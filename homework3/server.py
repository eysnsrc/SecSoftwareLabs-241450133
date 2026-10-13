from http.server import BaseHTTPRequestHandler, HTTPServer
import json

# 1. En az 8 adet güvenlik olayı (id, severity, type)
EVENTS = [
    {"id": 1, "severity": "low", "type": "failed-login"},
    {"id": 2, "severity": "high", "type": "bruteforce"},
    {"id": 3, "severity": "medium", "type": "unauthorized-access"},
    {"id": 4, "severity": "low", "type": "password-change"},
    {"id": 5, "severity": "high", "type": "malware"},
    {"id": 6, "severity": "medium", "type": "data-exfiltration"},
    {"id": 7, "severity": "low", "type": "account-locked"},
    {"id": 8, "severity": "high", "type": "suspicious-login"}
]

class SecurityHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Endpoint 1: Tüm olayları döndür
        if self.path == '/api/events':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(EVENTS).encode('utf-8'))
            
        # Endpoint 2: Sadece high severity olayları döndür
        elif self.path == '/api/events/high':
            high_events = [event for event in EVENTS if event['severity'] == 'high']
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(high_events).encode('utf-8'))
            
        # Endpoint 3: Olayların özetini döndür
        elif self.path == '/api/summary':
            summary = {
                "total": len(EVENTS),
                "low": sum(1 for e in EVENTS if e['severity'] == 'low'),
                "medium": sum(1 for e in EVENTS if e['severity'] == 'medium'),
                "high": sum(1 for e in EVENTS if e['severity'] == 'high')
            }
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(summary).encode('utf-8'))
            
        # Tanımlanmamış endpoint için 404 hatası
        else:
            self.send_response(404)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            error_response = {"error": "Endpoint not found"}
            self.wfile.write(json.dumps(error_response).encode('utf-8'))

# Sunucuyu başlatma fonksiyonu
def run(server_class=HTTPServer, handler_class=SecurityHandler, port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f"Sunucu http://localhost:{port} adresinde başlatıldı...")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    print("Sunucu kapatıldı.")

if __name__ == '__main__':
    run()