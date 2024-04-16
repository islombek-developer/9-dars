import csv
import requests
import threading
import time

start = time.perf_counter()

img_url = "https://docs.google.com/spreadsheets/d/1vpMsFooIDKq8RJ-9MVbEmjI4NlUCyxThByIi4frhcGQ/export?format=csv"

def img_download(url):
    try:
        response = requests.get(url)
        img_content = response.text
        img_name = "data.csv"  
        with open(img_name, "wb") as img_file:
            img_file.write(img_content)
            print(f"{img_name} downloaded")

    except Exception as e:
        print(f"Error  {url}: {e}")

threads = []
th = threading.Thread(target=img_download, args=[img_url])
th.start()
threads.append(th)

for t in threads:
    t.join()

end = time.perf_counter()
print(f"{end - start} second")
