'''
1.如果接收到的文字为’neko'，则发送一张猫片
'''
import itchat
import random
import os
@itchat.msg_register(itchat.content.TEXT)
def reply(msg):
	if msg['Text']=='neko':
		type=['.jpg','.gif','.png']      #由于类型有三种，这里做了一个数组，如果exist(fileDir)，那么就结束整个if块
		f_count=open('count.txt')
		count=f_count.read()
		count=int(count)
		N=random.randint(0,count)
		for image_type in type:
			print(image_type)
			fileDir=str(N)+image_type
			if os.path.exists(fileDir):
				print('ok')
				break
				
		print(fileDir)
		itchat.send_image(fileDir=fileDir,toUserName=msg['FromUserName'])
	return
itchat.auto_login(enableCmdQR=True,hotReload=True)		
itchat.run()
		