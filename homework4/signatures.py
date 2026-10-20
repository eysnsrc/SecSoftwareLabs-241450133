# SQL Injection Imzaları (Ödev örnekleri + ek özel imzalar)
SQLI_PATTERNS = [
    "or 1=1",
    "union select",
    "'--",
    "1=1--"
]

# XSS Imzaları (Ödev örnekleri + ek özel imzalar)
XSS_PATTERNS = [
    "<script",
    "javascript:",
    "onerror=",
    "alert("
]

# Path Traversal Imzaları (Ödev örnekleri + ek özel imzalar)
TRAVERSAL_PATTERNS = [
    "../",
    "..\\",
    "/etc/passwd",
    "system32"
]

# Saldırı türlerine göre Severity (Önem Seviyesi) Haritası
SEVERITY_MAP = {
    "SQL_INJECTION": "HIGH",
    "XSS": "HIGH",
    "PATH_TRAVERSAL": "MEDIUM"
}
