'''
查看百度开放平台官方文档
'''
from aip import AipOcr
from judge_car import judge_car
APP_ID=''
API_KEY=''
SECRET_KEY=''

client=AipOcr(APP_ID,API_KEY,SECRET_KEY)
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()
		
def send_car_image(image):
	result=judge_car(image)
	if result['result'][0]['name']=='非车类':
		return 'not car'
	else:
		options={}
		options['multi_detect']='true'
		result=client.licensePlate(get_file_content(image),options)
		#print(result['words_result'][0]['color']+'：'+result['words_result'][0]['number'])
		return result['words_result'][0]['color']+'：'+result['words_result'][0]['number']
		
if __name__=='__main__':
	send_car_image('car.jpg')