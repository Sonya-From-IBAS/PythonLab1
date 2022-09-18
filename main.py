import os
import requests
from bs4 import BeautifulSoup
from time import sleep

headers = {"User-Agent":"Mozilla/5.0"}

# headers = {
#     'User-Agent': ('Mozilla/5.0 (Windows NT 6.0; rv:14.0) Gecko/20100101 '
#                    'Firefox/14.0.1'),
#     'Accept':
#         'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#     'Accept-Language':
#         'ru-ru,ru;q=0.8,en-us;q=0.5,en;q=0.3',
#     'Accept-Encoding':
#         'gzip, deflate',
#     'Connection':
#         'keep-alive',
#     'DNT':
#         '1'
# }

if not os.path.isdir("dataset"):
    os.mkdir("dataset")
os.chdir("dataset")
if not os.path.isdir("rose"):
    os.mkdir("rose")
if not os.path.isdir("tulip"):
    os.mkdir("tulip")


def download_image(url_image, name, item):
    src = requests.get(url_image, stream=True)
    with open(f'{item}/{name}.jpg', 'ab') as file:
        for iteration in src.iter_content(1024**2):
            file.write(iteration)
    file.close()


def get_image_url(item):
    for page in range(1, 35):
        url = f'https://yandex.ru/images/search?p={page}&text={item}'
        src = requests.get(url, headers=headers)
        soup = BeautifulSoup(src.text, "lxml")
        all_images = soup.find_all("a", class_="serp-item__link")
        for image in all_images:
            url_img = "https:" + image.find("img", class_="serp-item__thumb").get("src")
            yield url_img


number = 0
for url_of_item in get_image_url("rose"):
    number += 1
    download_image(url_of_item, str(number).zfill(4), "rose")
    print(1)
    sleep(1)

number = 0
for url_of_item in get_image_url("tulip"):
    number += 1
    download_image(url_of_item, str(number).zfill(4), "tulip")
    print(2)
    sleep(1)




