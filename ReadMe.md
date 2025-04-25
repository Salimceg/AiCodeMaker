Yapay Zeka Destekli Kod Üretici

Bu proje, kullanıcının girdisiyle OpenAI API'si aracılığıyla Python kodu ve başlığı üreten bir Flask web uygulamasıdır. Docker ile container haline getirilmiştir.

📆 Teknolojiler

Python 3.12

Flask

OpenAI API (gpt-3.5-turbo)

HTML (Jinja2 ile render)

Docker

🛠️ Kurulum ve Çalıştırma

1. Projeyi Klonlayın

git clone <repo-link>
cd Myproject.py

2. OpenAI API Key Ayarla

config.py içine aşağıdaki şekilde API anahtarını ekleyin:

OPENAI_API_KEY = "sk-..."

3. Docker Build

docker build -t ai-kod-uretici .

4. Docker Container Çalıştır

docker run -p 5050:5000 ai-kod-uretici

5. Tarayıcıdan Eriş

http://localhost:5050

🌍 Dockerfile Özeti

FROM python:3-slim
COPY requirements.txt .
RUN python -m pip install -r requirements.txt
WORKDIR /app
COPY . /app
CMD ["python", "app.py"]

📋 Dosya Yapısı

Myproject.py/
├── app.py
├── config.py
├── requirements.txt
├── Dockerfile
├── templates/
│   └── index.html

❌ Karşılaşılabilecek Sorunlar

API RateLimitError: API key kotası dolmuş olabilir.

Port already in use: 5000 portunda başka bir uygulama çalışıyor olabilir.

Sayfa açılmıyor: Doğru porta (localhost:5050) gittiğinizden emin olun.

✨ Öneriler

Kod bloklarını daha güzel göstermek için Prism.js veya highlight.js entegre edebilirsin.

OpenAI isteği için hata kontrolü (try-except) eklenebilir.

Kullanıcıdan prompt almak için input alanına placeholder eklenebilir.

📤 Lisans

MIT