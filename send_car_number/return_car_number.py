import itchat
from send_car_image import send_car_image
Name=[]
@itchat.msg_register(itchat.content.PICTURE)
def reply(msg):
	car_image=msg['Text'](msg['FileName'])
	result=send_car_image(msg['FileName'])
	if result=='not car':
		return 
	else:
		itchat.send_msg(msg=result,toUserName=msg['FromUserName'])
		return
itchat.auto_login(enableCmdQR=True,hotReload=True)		
itchat.run()
		
		
