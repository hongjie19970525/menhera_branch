import itchat
Name=[]
from translate import trans
@itchat.msg_register(itchat.content.TEXT)
def reply(msg):
	global Name
	if msg['Text']=='翻译' and msg['FromUserName'] not in Name:
		Name.append(msg['FromUserName'])
		itchat.send_msg(msg='进入翻译，请输入英文',toUserName=msg['FromUserName'])
		return
	if msg['FromUserName'] in Name and msg['Text']!='退出':
		result=trans(msg['Text'])
		itchat.send_msg(msg=result,toUserName=msg['FromUserName'])
		return 
	if msg['Text']=='退出' and msg['FromUserName'] in Name:
		Name.remove(msg['FromUserName'])
		return
		
itchat.auto_login(enableCmdQR=True,hotReload=True)		
itchat.run()
	