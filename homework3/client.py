import requests
import csv

# Sunucu adresi
BASE_URL = "http://localhost:8000/api/events"
TIMEOUT_SEC = 5

def main():
    try:
        # 1. API'ye GET isteği at (timeout ile)
        response = requests.get(BASE_URL, timeout=TIMEOUT_SEC)
        
        # 404 gibi HTTP hatalarını yakalamak için
        response.raise_for_status()
        
        # Gelen JSON verisini Python listesine/sözlüğüne çevir
        events = response.json()
        
        # 2. İstenen hesaplamalar
        total_events = len(events)
        low_count = sum(1 for e in events if e.get('severity') == 'low')
        medium_count = sum(1 for e in events if e.get('severity') == 'medium')
        high_count = sum(1 for e in events if e.get('severity') == 'high')
        
        # 3. Yalnızca high severity olaylarını filtrele
        high_events = [e for e in events if e.get('severity') == 'high']
        
        # 4. Çıktıları ekrana yazdır (Örnek çıktı formatında)
        print("API bağlantısı başarılı.\n")
        print(f"Toplam olay: {total_events}\n")
        
        print("Severity dağılımı:")
        print(f"LOW    : {low_count}")
        print(f"MEDIUM : {medium_count}")
        print(f"HIGH   : {high_count}\n")
        
        print("HIGH SEVERITY EVENTS")
        for event in high_events:
            print(f"ID: {event['id']}")
            print(f"Type: {event['type']}\n")
            
        # 5. CSV Çıktısını Kaydetme
        with open("high_events.csv", mode="w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["id", "severity", "type"]) # Başlık
            for event in high_events:
                writer.writerow([event["id"], event["severity"], event["type"]])
                
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP hatası: {response.status_code}")
    except requests.exceptions.ConnectionError:
        print("API sunucusuna bağlanılamadı.")
    except requests.exceptions.Timeout:
        print("Bağlantı zaman aşımına uğradı (Timeout).")
    except Exception as err:
        print(f"Bilinmeyen bir hata oluştu: {err}")

if __name__ == "__main__":
    main()
