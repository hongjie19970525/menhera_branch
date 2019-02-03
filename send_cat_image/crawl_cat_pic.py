'''
通过requests.get('https://api.thecatapi.com/v1/images/search')获取猫片的下载地址
该接口返回一个下载地址
再通过requests.get这个地址，可将猫片下载到本地，注意get的时候要带上HEADERS，不然好像无法下载
图片格式包括png，gif,jpg，命名规则我这里是读取外部的数字来当作文件名
'''

import requests
import time

HEADERS={
	"X-Requested-With":"XMLHttpRequest",
	"User-Agent":"Mozilla/5.0(Windows NT 10.0;WOW64)AppleWebKit/537.36"
	"(KHTML,like Gecko)Chrome/56.0.2924.87 Safari/537.36",
	}
	

i=0
while True:
	f_count=open('count.txt')
	count=f_count.read()
	f_count.close()
	count=int(count)
	
	url_image=requests.get('https://api.thecatapi.com/v1/images/search').json()
	print(url_image)
	print(url_image[0]['url'])
	url=url_image[0]['url']
	print(url)
	try:
		r_image=requests.get(url,headers=HEADERS,timeout=5)
	except:
		continue
	#print(r_image)
	type=url.split('.')[3]
	image_name=str(count)+'.'+type
	fp=open(image_name,'wb')
	fp.write(r_image.content)
	fp.close()
	count=count+1
	
	f_count=open('count.txt','w+')
	f_count.write(str(count))
	f_count.close()
	
	i=i+1
	time.sleep(10)