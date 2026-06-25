"""
    This script is used visit each project I've deployed to prevent them from sleep. 
"""

import requests

urls = [
    "https://nick-kevin-track-popularity.hf.space/",
    "https://nick-kevin-credit-scoring-ai.hf.space/",
]

# add a User-Agent header to your request
# Streamlit's servers block or endlessly redirect basic automated scripts
# that use Python's default urllib user agent string to protect themselves against bot 

# Real browser headers
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.5"
}


for url in urls:
    try:
        with requests.Session() as session:
            session.headers.update(HEADERS)

            # allow_redirects=True explicitly tells Python to follow Streamlit's routing paths
            response = session.get(url, timeout=20, allow_redirects=True)
               
            print("------------------------------------")
            print(f"Ping successful! Final URL reached: {response.url}")
            print(f"Response Status Code: {response.status_code}")
    except ValueError:
        print(f"Ping {url} failed: the website is sleeping")
        print(f"Error: {ValueError}")
