# API与微信自动回复的组合
branch of menhera
## 获取机动车牌照
### 通过[百度AI平台](www.ai.baidu.com)识别车辆中的牌照，回传至微信
1.  拍照人将照片上传至微信
2.  微信将1中的照片下载至本地
3.  将本地照片上传至车辆设别接口
4.  若3回传是为机动车辆，那么调用车辆牌照识别接口
5.  通过微信将4返回的值传回给拍照人
python send_car_number/return_car_number.py

## 翻译
### 通过[百度翻译平台](api.fanyi.baidu.com)获取翻译内容，回传至微信
当前只支持汉译英
python send_trans_result/send_trans_result.py

## 下载猫片
偶尔看到一个很好用的下载猫片接口，通过调用，可无限制下载猫片，可将猫片上传至微信
python send_car_image/send_cat_pic.py
