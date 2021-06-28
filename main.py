import requests
import time
import os
from io import BytesIO
from PIL import Image
from bs4 import BeautifulSoup

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106 Safari/537.36'}
r = requests.get('https://lambert-lambert.com/talents/charles-negre', headers=headers)
print(r.status_code)
soup = BeautifulSoup(r.text, 'html.parser')
imgs = soup.find_all('img', class_='lazy')
#定义图片下载目录
save_path=os.getcwd()+'/photo'
if os.path.exists(save_path) == False:
    os.makedirs(save_path)
for index,img in enumerate(imgs):
    src=img.get('data-src')
    if src is not None:
        html=requests.get(src)
        img_name='lambert_'+str(index+1)+'.png'
        image=Image.open(BytesIO(html.content))
        image.save(save_path+'/'+img_name)
        print('第'+str(index+1)+'张图片下载完成')
        time.sleep(1)
print('下载完成')
