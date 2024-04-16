import csv
import requests
import threading
import time

start = time.perf_counter()

txt_url = "https://docs.google.com/spreadsheets/d/1vpMsFooIDKq8RJ-9MVbEmjI4NlUCyxThByIi4frhcGQ/export?format=csv"

def txt_download(url):
    try:
        response = requests.get(url)
        txt_content = response.text
        txt_name = "data.csv"  
        with open(txt_name, "w") as txt_file:
            txt_file.write(txt_content)
            print(f"{txt_name} downloaded")

    except Exception as e:
        print(f"Error  {url}: {e}")

threads = []
th = threading.Thread(target=txt_download, args=[txt_url])
th.start()
threads.append(th)

for t in threads:
    t.join()

end = time.perf_counter()
print(f"{end - start} second")
