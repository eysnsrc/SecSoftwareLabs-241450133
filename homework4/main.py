import json
import csv
from detector import detect_attack

def main():
    # 1. JSON dosyasından test isteklerini okuma (Hatalı veri kontrolü ile)
    try:
        with open("test_requests.json", "r", encoding="utf-8") as f:
            requests = json.load(f)
    except Exception as e:
        print(f"JSON dosyası okunurken hata oluştu: {e}")
        return

    alerts = []
    stats = {
        "total": 0,
        "allowed": 0,
        "blocked": 0,
        "SQL_INJECTION": 0,
        "XSS": 0,
        "PATH_TRAVERSAL": 0
    }

    print("=== WAF ANALİZ BAŞLATILDI ===\n")

    # 2. Her isteği analiz etme
    for req in requests:
        stats["total"] += 1
        
        src_ip = req.get("src_ip", "UNKNOWN") if isinstance(req, dict) else "UNKNOWN"
        method = req.get("method", "UNKNOWN") if isinstance(req, dict) else "UNKNOWN"
        url = req.get("url", "") if isinstance(req, dict) else ""

        attack, severity, action = detect_attack(req)

        # İstatistikleri ve uyarı listesini güncelleme
        if action == "BLOCK":
            stats["blocked"] += 1
            if attack in stats:
                stats[attack] += 1
            alerts.append({
                "src_ip": src_ip,
                "method": method,
                "url": url,
                "attack": attack,
                "severity": severity,
                "action": action
            })
        else:
            stats["allowed"] += 1

        # Sonuçları ekrana yazdırma (Gereksinim 8)
        print(f"IP       : {src_ip}")
        print(f"URL      : {url}")
        print(f"Attack   : {attack if attack else 'NONE'}")
        print(f"Severity : {severity}")
        print(f"Action   : {action}")
        print("-" * 40)

    # 3. Saldırı tespit edilenleri alerts.csv dosyasına kaydetme (Gereksinim 9)
    fieldnames = ["src_ip", "method", "url", "attack", "severity", "action"]
    with open("alerts.csv", "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(alerts)

    # 4. İstatistik Özetini Yazdırma (Gereksinim 10)
    print("\n=== İSTATİSTİK ÖZETİ ===")
    print(f"Toplam Request : {stats['total']}")
    print(f"Allowed        : {stats['allowed']}")
    print(f"Blocked        : {stats['blocked']}\n")
    print(f"SQL Injection  : {stats['SQL_INJECTION']}")
    print(f"XSS            : {stats['XSS']}")
    print(f"Path Traversal : {stats['PATH_TRAVERSAL']}")
    print("========================\n")
    print("Saldırı kayıtları 'alerts.csv' dosyasına yazıldı.")

if __name__ == "__main__":
    main()