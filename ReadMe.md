Yapay Zeka Destekli Kod Üretici

Bu proje, kullanıcının girdisiyle OpenAI API'si aracılığıyla Python kodu ve başlığı üreten bir Flask web uygulamasıdır. Docker ile container haline getirilmiştir.

📆 Teknolojiler

Python 3.12

Flask

OpenAI API (gpt-3.5-turbo)

HTML (Jinja2 ile render)

Docker

🛠️ Kurulum ve Çalıştırma

🔁 Repoyu Klonla

git clone https://github.com/Salimceg/AiCodeMaker.git
cd AiCodeMaker

🔐 OpenAI API Anahtarını Tanımla

config.py dosyası oluştur:

touch config.py

İçeriği şöyle olsun:

OPENAI_API_KEY = "sk-..."  # Buraya kendi OpenAI API key'ini yaz

🐳 Docker ile Çalıştırmak için

1. Docker Image Oluştur

docker build -t ai-kod-uretici .

2. Docker Container Başlat

docker run -p 5050:5000 ai-kod-uretici

3. Tarayıcıdan Eriş

http://localhost:5050

🧪 Alternatif: Docker Olmadan Çalıştırma

1. Sanal Ortam Oluştur

python3 -m venv .venv
source .venv/bin/activate

2. Gereken Kütüphaneleri Yükle

pip install -r requirements.txt

3. Uygulamayı Başlat

python app.py

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
├── config.py (repoya dahil değil)
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

