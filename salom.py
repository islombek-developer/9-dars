import time
import requests
start=time.perf_counter()
img_urls = [
    'https://images.unsplash.com/photo-1516117172878-fd2c41f4a759',
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
for imeg in img_urls:
    img_connect=requests.get(imeg).content
    img_name=f"{imeg.split('/')[-1]}.jpg"
    with open(img_name,"wb") as img_file:
        img_file.write(img_connect)
        print(f"{img_name} dowload")

end=time.perf_counter()
print(f"{end-start} tugadi")

















# import threading

# start=time.perf_counter()
# def foo(num):
#     print(f"Hello word {num} seconds ...")
#     print("tugadi")
# threads=[]
# for i in range(15):
#     t=threading.Thread(target=foo, args=[5])
#     t.start()
#     threads.append(t)
# for i in threads:
#     i.join()
# end=time.perf_counter()
# print(f"salom {start-end}")

# import time
# import threading
# start=time.perf_counter()
# def foo():
#     print("1 second otdi")
#     time.sleep(0.1)
#     print("tugadi")
# threads=[]
# for i in range(15):
#     t=threading.Thread(target=foo)
#     t.start()
#     threads.append(t)
# for i in threads:
#     i.join()

# end=time.perf_counter()
# print(f"tugatildi {end-start} shu vaqtda")

# import time
# import threading
# start=time.perf_counter()
# def foo(second,num):
#     print(f"{num} second otdi")
#     time.sleep(second)
#     print("tugadi")
# threads=[]
# for i in range(10):
#     t=threading.Thread(target=foo, args=[1,5])
#     t.start()
#     threads.append(t)
# for i in threads:
#     i.join()

# end=time.perf_counter()
# print(f"tugatildi {end-start} shu vaqtda")