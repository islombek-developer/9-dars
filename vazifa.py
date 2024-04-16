
import requests
import threading
import time

start = time.perf_counter()

img_urls = ["Users\HP\Desktop "]

def img_download(img_url):
    try:
        img_name = f"{img_url.split()}.txt"
        with open(img_name, "wb") as img_file:
            img_file.write(img_content)
            print(f"{img_name} downloaded")
    except:
        with open("img_name", "wb") as img_file:
            img_file.write("xatolik bor 404")
threads = []
for image_url in img_urls:
    th = threading.Thread(target=img_download, args=[image_url])
    th.start()
    threads.append(th)

for t in threads:
    t.join()

end = time.perf_counter()
print(f"{end - start} seconds elapsed")