# Homework 2 - JSON, Regex, CSV ve Veri Doğrulama

## Ödevin Amacı

Bu ödevin amacı JSONL formatındaki bir veri dosyasını Python ile okumak, verileri filtrelemek, IP adreslerini Regex kullanarak doğrulamak ve sonuçları CSV dosyasına aktarmaktır.

## Kullanılan Veri Seti

Program, `events.jsonl` veri setini kullanmaktadır.

## Programın Çalıştırılması

Program terminal üzerinden aşağıdaki komut ile çalıştırılır:

    py week03_regex_json.py

## Programın Yaptığı İşlemler

- `events.jsonl` dosyasını satır satır okur.
- Her satırı JSON olarak parse eder.
- Toplam olay sayısını hesaplar.
- `status` değeri `FAILED` olan kayıtları filtreler.
- `src_ip` alanını Regex kullanarak doğrular.
- Geçerli IP adresine sahip `FAILED` kayıtlarını seçer.
- Hatalı JSON satırlarını `try/except` kullanarak atlar.
- Sonuçları `failed_events.csv` dosyasına kaydeder.

## Örnek Çıktı

    Total events: 35
    Failed events: 16
    CSV oluşturuldu: failed_events.csv