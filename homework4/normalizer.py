import re
from urllib.parse import unquote

def normalize(value):
    """
    URL verisini decode eder, küçük harfe çevirir ve 
    birden fazla boşluğu tek boşluğa düşürerek normalize eder.
    """
    if not isinstance(value, str):
        return ""
    
    # 1. URL Decode (%27 -> ', %20 -> boşluk)
    decoded = unquote(value)
    
    # 2. Küçük harfe çevirme
    lowercased = decoded.lower()
    
    # 3. Birden fazla yan yana boşluğu tek boşluğa düşürme ve kenar boşluklarını temizleme
    normalized_value = re.sub(r'\s+', ' ', lowercased).strip()
    
    return normalized_value
