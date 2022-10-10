# 测物流的接口
# pytest。unittest 前置条件  获得加密的数据  放在 showapi_sign里面
from hashlib import md5

import requests

url='http://route.showapi.com/64-34'
data={
    'com':'yuantong',
    'nu':'YT6493188734653',
    'showapi_appid':'1033673',
    'showapi_sign':'comyuantongnuYT6493188734653showapi_appid10336736d4a4cd45d63490cad71d4afde685242'
}
s=requests.post(url,data)
print(s.json())

# 键值对  不限于这种写法  加密  规则  项目中 规则 灵活的写 换一个名字也能拼接
# 封装在一个函数里面  要用的时候 直接调用函数  reduce 逻辑比较麻烦
a='com'+data['com']+'nu'+data['nu']+'showapi_appid'+data['showapi_appid']
print(a)

# 进行md5加密 不可逆  不能进行解密 加盐加密方式 比md5更加安全

ret=md5(a.encode(encoding='UTF-8')).hexdigest()
print(ret)


