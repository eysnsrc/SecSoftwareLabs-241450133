# Homework 3 - Mini Security Event API

Bu proje, Python kullanarak basit bir güvenlik olayları REST API sunucusu (`server.py`) ve bu API'den veri çeken, analiz eden ve filtrelenen verileri CSV dosyasına kaydeden bir istemci (`client.py`) uygulaması içerir.

## Ödevin Amacı
HTTP, REST API, JSON formatı, HTTP durum kodları, bağlantı zaman aşımı (timeout) ve hata yönetimi kavramlarını hem sunucu hem istemci tarafında uygulamalı olarak göstermektir.

## Kullanılan Endpoint'ler
* `GET /api/events`: Tüm güvenlik olaylarını JSON formatında döndürür.
* `GET /api/events/high`: Sadece öncelik seviyesi (severity) "high" olan olayları döndürür.
* `GET /api/summary`: Toplam olay sayısını ve önem seviyelerine göre dağılım özetini döndürür.
* Tanımlanmamış endpoint'ler: `404 Not Found` durum kodu ile `{"error": "Endpoint not found"}` hatası döndürür.

## Uygulamaların Çalıştırılması

1. **Sunucunun Başlatılması:**
   `homework3` klasöründe terminal açarak şu komut çalıştırılır:
   ```bash
   py server.py