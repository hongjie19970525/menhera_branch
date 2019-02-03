'''
查看百度开放平台官方文档
'''
from aip import AipImageClassify
APP_ID=''
API_KEY=''
SECRET_KEY=''

client=AipImageClassify(APP_ID,API_KEY,SECRET_KEY)
def get_file_content(filepath):
	with open(filepath,'rb') as fp:
		return fp.read()
		
def judge_car(image):
	result=client.carDetect(get_file_content(image))
	print(result)
	return result
	
if __name__=='__main__':
	judge_car(get_file_content('car.jpg'))