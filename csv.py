import threading
import time
from bs4 import BeautifulSoup
import requests
start = time.perf_counter()
import csv
tables = [
        'https://bank.uz/currency#RUB'
]

def table(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser') 
        text_content = soup.get_text()  
        file_name = f"{url.split('/')[-1]}.csv"
        with open(file_name, "w", encoding="utf-8") as text_file:
            text_file.write(text_content)
            print(f"{file_name} downloaded")
    except Exception as e:
        print(f"Error {url}: {e}")

threads = []
for url in tables:
    thread = threading.Thread(target=table, args=[url])
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()

end = time.perf_counter()
print(f"{end - start} seconds elapsed")