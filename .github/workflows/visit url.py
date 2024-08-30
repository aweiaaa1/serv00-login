import requests

urls = [
    "https://example.com",
    "https://another-example.com",
    "https://yet-another-example.com"
]

for url in urls:
    try:
        response = requests.get(url)
        print(f"Visited {url}: Status Code {response.status_code}")
        # 可选：输出响应的前200个字符
        print(f"Content (first 200 chars): {response.text[:200]}")
    except requests.RequestException as e:
        print(f"Error visiting {url}: {e}")
