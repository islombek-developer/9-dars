import requests
import threading
import time

start = time.perf_counter()

img_urls = [
    'https:images.unsplash.comphoto-1516117172878-fd2c41f4a759',
    'https://images.unsplash.com/photo-1532009324734-20a7a5813719',
    'https://images.unsplash.com/photo-1524429656589-6633a470097c',
    'https://images.unsplash.com/photo-1530224264768-7ff8c1789d79',
    'https://images.unsplash.com/photo-1564135624576-c5c88640f235',
    'https://images.unsplash.com/photo-1541698444083-023c97d3f4b6',
    'https://images.unsplash.com/photo-1522364723953-452d3431c267',
    'https://images.unsplash.com/photo-1513938709626-033611b8cc03',
    'https://images.unsplash.com/photo-1507143550189-fed454f93097',
    'https://images.unsplash.com/photo-1493976040374-85c8e12f0c0e',
    'https://images.unsplash.com/photo-1504198453319-5ce911bafcde',
    'https://images.unsplash.com/photo-1530122037265-a5f1f91d3b99',
    'https://images.unsplash.com/photo-1516972810927-80185027ca84',
    'https://images.unsplash.com/photo-1550439062-609e1531270e',
    'https://images.unsplash.com/photo-1549692520-acc6669e2f0c'
]

def img_download(img_url):
    try:
        img_content = requests.get(img_url).content
        img_name = f"{img_url.split('/')[-1]}.jpg"
        with open(img_name, "wb") as img_file:
            img_file.write(img_content)
            print(f"{img_name} downloaded")
    except :
        with open("img_name", "w") as img_file:
            img_file.write("sizda xatolik bor 404")
        

threads = []
for image_url in img_urls:
    th = threading.Thread(target=img_download, args=[image_url])
    th.start()
    threads.append(th)

for t in threads:
    t.join()

end = time.perf_counter()
print(f"{end - start} seconds elapsed")