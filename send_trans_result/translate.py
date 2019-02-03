'''
查看百度翻译平台官方文档
'''
#coding=utf8
import requests
import hashlib
import random
def trans(msg):
	#MD5=hashlib.md5()
	APPID='20190202000262070'
	SECRETKEY='lb5D0JNbcDiFhE_m4_q_'
	URL='http://api.fanyi.baidu.com/api/trans/vip/translate'
	q=msg
	FromLang='en'
	ToLang='zh'
	salt = random.randint(32768, 65536)
	salt=str(salt)
	sign=hashlib.md5((APPID+q+salt+SECRETKEY).encode('utf-8')).hexdigest()
	params={'q':q,'from':FromLang,'to':ToLang,'appid':APPID,'salt':salt,'sign':sign}
	r=requests.get(URL,params=params).json()
	print(r['trans_result'][0]['dst'])
	return r['trans_result'][0]['dst']


