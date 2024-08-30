import requests

urls = [
    "https://yingshi1.aweiawym.us.kg/api.php/timming/index.html?enforce=1&name=dd",
    "https://yingshi1.aweiawym.us.kg/api.php/timming/index.html?enforce=1&name=cc",
]

for url in urls:
    try:
        response = requests.get(url)
        print(f"Visited {url}: Status Code {response.status_code}")
        # 可选：输出响应的前200个字符
        print(f"Content (first 200 chars): {response.text[:200]}")
    except requests.RequestException as e:
        print(f"Error visiting {url}: {e}")
