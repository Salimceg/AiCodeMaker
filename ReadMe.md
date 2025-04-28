

Yapay Zeka Destekli Kod Üretici
-Bu proje, kullanıcının girdisiyle Python kodu ve başlık üreten bir Flask web uygulamasıdır. -Ollama yerel LLM kullanımı ile çalışır, ayrıca Docker container haline getirilmiştir.
-Teknolojiler:
*Python 3.12
*Flask
*Ollama API (yerel LLM)
* HTML (Jinja2 template sistemi) 
*Docker
————————————————
Kurulum ve Çalıştırma
-Repoyu Klonla:
bash/ git clone https://github.com/Salimceg/OllamaCodeMakerr.git bash/ cd OllamaCodeMakerr
-Ollama Kurulumu ve Başlatılması:
bash/ brew install ollama bash/ ollama serve
-Yeni terminal açıp:
bash/ ollama run mistral (Mistral modeli indirilip arka planda çalışacak)
-Local Sanal Ortam Kurulumu:
bash/ python3 -m venv .venv bash/ source .venv/bin/activate
-Gerekli Kütüphaneleri Kur:
bash/ pip install -r requirements.txt
-Uygulamayı Başlat:
bash/ python3 app.py
-Uygulama Tarayıcıdan Erişimi:
http://localhost:5055
-Eğer 5055 portu doluysa:
bash/ lsof -i :5055 bash/ kill -9 PID veya başka bir port kullanılmalı
Docker ile Çalıştırmak
-Docker Image oluştur:
bash/ docker build -t ai-kod-uretici .
-Docker Container başlat:
bash/ docker run -p 5050:5000 ai-kod-uretici
-Tarayıcıdan erişim:
http://localhost:5050
Dockerfile Özeti
FROM python:3-slim COPY requirements.txt . RUN python -m pip install -r requirements.txt WORKDIR /app COPY . /app CMD ["python", "app.py"]
Dosya Yapısı
OllamaCodeMakerr/
* app.py
* requirements.txt
* Dockerfile
* templates/
    * index.html
(Opsiyonel: config.py dosyası oluşturulabilir, API anahtarı vs. için.)
Olası Problemler
-API bağlantı hatası: Ollama'nın arka planda çalışıp çalışmadığı kontrol edilmeli. -Port dolu hatası: lsof -i :5055 ve kill -9 PID komutları ile temizlenmeli. -Request modülü bulunamadı hatası: bash/ pip3 install requests -Docker veya Minikube üzerinde çalışırken ImagePull hatası alınırsa image build edilip tekrar deploy edilmeli.
