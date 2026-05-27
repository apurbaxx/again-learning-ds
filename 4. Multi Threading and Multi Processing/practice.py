import threading

import requests
from bs4 import BeautifulSoup

urls = [
    "https://reference.langchain.com/python/langchain",
    "https://reference.langchain.com/python/langchain/middleware",
    "https://reference.langchain.com/python/langchain/agents",
]


def fetch_content(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    print(f"Fetched total of {len(soup.text)} from this url={url}")


threads = []
for url in urls:
    thread = threading.Thread(target=fetch_content, args=(url,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()
