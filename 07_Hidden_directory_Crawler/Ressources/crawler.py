import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def crawl(url, visited):
    if url in visited:
        return

    visited.add(url)
    print(f"Crawling: {url}")

    try:
        response = requests.get(url, timeout=10)
    except requests.RequestException as e:
        print(f"Failed to retrieve {url}: {e}")
        return

    if response.status_code != 200:
        print(f"Failed to retrieve {url}: status code {response.status_code}")
        return

    soup = BeautifulSoup(response.content, 'html.parser')
    for element in soup(text=lambda text: 'flag' in text.lower()):
        print(f"Found 'flag' on page: {url}")
        print(f"Flag: {element}")
        exit()

    for link in soup.find_all('a', href=True):
        next_url = urljoin(url, link['href'])
        if next_url not in visited and "http://127.0.0.1:8080/.hidden/" in next_url:
            crawl(next_url, visited)

if __name__ == "__main__":
    visited = set()
    start_url = 'http://127.0.0.1:8080/.hidden/'
    crawl(start_url, visited)
