from flask import Flask, render_template, request
from openai import OpenAI
from config import OPENAI_API_KEY

app = Flask(__name__)
client = OpenAI(api_key=OPENAI_API_KEY)

@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")

@app.route("/generate", methods=["POST"])
def generate():
    prompt = request.form["prompt"]

    full_prompt = f"""
You are a helpful Python coding assistant. First, generate a short descriptive title. Then write Python code that fulfills the user's request.

User request: {prompt}
"""

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a professional Python developer."},
            {"role": "user", "content": full_prompt}
        ],
        temperature=0.7,
        max_tokens=500
    )

    result = response.choices[0].message.content.strip()

    parts = result.split("\n", 1)
    title = parts[0].replace("Title:", "").strip()
    code = parts[1].strip() if len(parts) > 1 else "Kod üretilemedi."

    return render_template("index.html", title=title, code=code)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

