# Homework 4 - Mini WAF ve Web Attack Detector

Bu proje, kural tabanlı bir Web Application Firewall (WAF) ve web saldırı tespit motorudur. Gelen HTTP isteklerini URL decode ve normalize işlemlerinden geçirerek SQL Injection (SQLi), Cross-Site Scripting (XSS) ve Path Traversal saldırılarını tespit eder, loglar ve duruma göre engelleme kararı verir.

## Projenin Amacı
Gelen HTTP istek metinlerini güvenlik süzgecinden geçirerek bilinen saldırı kalıplarını tespit etmek, zararlı istekleri engellemek (BLOCK) ve tespit edilen saldırıları `alerts.csv` dosyasına kaydetmektir.

## Dosya Yapısı
* `test_requests.json`: Test senaryoları için normal, saldırı içeren, URL encoded ve hatalı request verileri.
* `normalizer.py`: Gelen URL verilerini decode eden, küçük harfe dönüştüren ve boşlukları temizleyen modül.
* `signatures.py`: SQLi, XSS ve Path Traversal için tanımlanmış saldırı kalıpları (imzalar) ve severity haritası.
* `detector.py`: İmzaları kontrol eden, hatalı/eksik veri yönetimini sağlayan tespit motoru.
* `main.py`: İstekleri okuyan, tespit akışını çalıştıran, istatistik sunan ve `alerts.csv` oluşturan ana betik.
* `alerts.csv`: Sadece engellenen zararlı isteklerin kaydedildiği çıktı dosyası.
* `README.md`: Proje dokümantasyonu ve test raporu.

## Çalıştırma
`homework4` klasöründe terminal açarak şu komut çalıştırılır:
```bash
py main.py