import re
from urllib.parse import urlparse

def extract_features(url):
    parsed = urlparse(url)

    # Count dots in URL
    dots = url.count('.')

    # URL length
    length = len(url)

    # Check if URL contains IP address
    has_ip = 1 if re.match(r"\d+\.\d+\.\d+\.\d+", parsed.netloc) else 0

    # Special characters
    special_chars = sum([url.count(c) for c in ['@', '?', '-', '=', '.', '#', '%']])

    # HTTPS check
    is_https = 1 if parsed.scheme == "https" else 0

    # Count number of "/" (link depth)
    link_count = url.count('/')

    return [dots, length, has_ip, special_chars, is_https, link_count]

