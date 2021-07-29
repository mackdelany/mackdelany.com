import os
from pathlib import Path

from airium import Airium

PATH_TO_IMGS = './static/imgs/life/'

files = os.listdir('.')
imgs = [f for f in files if '.jp' in f]


def get_img_title(filename: str) -> str:
    return filename.replace('_', ' ').split('.')[0]


a = Airium()
for img in imgs:
    img_tile = get_img_title(img)
    with a.div(klass="memory-generator-card"):
        a.img(src=str(Path(PATH_TO_IMGS, img)), alt=img_tile, klass="memory-generator-img")
        a(img_tile)

html_str = str(a)
print(html_str)