import requests
import threading
import time
from bs4 import BeautifulSoup

start = time.perf_counter()

text_urls = [
    'https://uz.wikipedia.org/wiki/Arslon',
    'https://bank.uz/currency#RUB',
    'https://www.bbc.com/news'
]

def write_text(url):
    try:
        response = requests.get(url)
        result = BeautifulSoup(response.content, 'html.parser') 
        text_content = result.get_text()  
        file_name = f"{url.split('/')[-1]}.txt"
        with open(file_name, "w", encoding="utf-8") as text_file:
            text_file.write(text_content)
            print(f"{file_name} kochirildi")
    except Exception as e:
        print(f"Error {url}: {e}")

threads = []
for url in text_urls:
    thread = threading.Thread(target=write_text, args=[url])
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()

end = time.perf_counter()
print(f"{end - start} second")
