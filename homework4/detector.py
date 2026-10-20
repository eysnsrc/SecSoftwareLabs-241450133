from normalizer import normalize
from signatures import SQLI_PATTERNS, XSS_PATTERNS, TRAVERSAL_PATTERNS, SEVERITY_MAP

def detect_sqli(normalized_url):
    """Normalized URL içerisinde SQL Injection imzası arar."""
    for pattern in SQLI_PATTERNS:
        if pattern in normalized_url:
            return "SQL_INJECTION"
    return None

def detect_xss(normalized_url):
    """Normalized URL içerisinde XSS imzası arar."""
    for pattern in XSS_PATTERNS:
        if pattern in normalized_url:
            return "XSS"
    return None

def detect_traversal(normalized_url):
    """Normalized URL içerisinde Path Traversal imzası arar."""
    for pattern in TRAVERSAL_PATTERNS:
        if pattern in normalized_url:
            return "PATH_TRAVERSAL"
    return None

def detect_attack(request):
    """
    Gelen request sözlüğünü analiz eder.
    Hatalı/eksik veri yönetimi (Gereksinim 13) yaparak uygulamanın çökmesini engeller.
    Saldırı türü, severity ve action (ALLOW/BLOCK) döndürür.
    """
    # 1. Hatalı Veri Kontrolü (request bir sözlük değilse)
    if not isinstance(request, dict):
        return None, "NONE", "ALLOW"
    
    # 2. URL Alanı Kontrolü (URL yoksa veya dize değilse)
    raw_url = request.get("url")
    if not raw_url or not isinstance(raw_url, str):
        return None, "NONE", "ALLOW"
    
    # 3. URL Normalization
    normalized_url = normalize(raw_url)
    
    # 4. Saldırı Tespiti
    attack_type = (
        detect_sqli(normalized_url) or 
        detect_xss(normalized_url) or 
        detect_traversal(normalized_url)
    )
    
    # 5. Karar Mekanizması (ALLOW / BLOCK ve Severity)
    if attack_type:
        severity = SEVERITY_MAP.get(attack_type, "MEDIUM")
        action = "BLOCK"
        return attack_type, severity, action
    
    return None, "NONE", "ALLOW"
