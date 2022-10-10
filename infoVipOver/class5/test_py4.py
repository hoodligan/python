# 3.把token放在session中
# session:英文  开会 会议
# 编程：一次会话
# 登录--下单--支付 session
# 登录开始 会话开始建立  系统任何操作  session存放了会话过程中任何对象
# 浏览器关闭 session会话就结束了

# 登录进去了  token放在session里面  记录到我了  我在里面做的操作 都会知道是谁做的
# 你在session去访问  访问  登录 session    关闭
import allure
import jsonpath
import pytest
import requests

# 1.创建session对象
# 2.设置session的headers属性  token放进去
from class3.httpclient import HttpClient

# 数据都是放在业务代码里面  数据提取出来
from class5.base.yamlload import YamlUtil


@allure.feature('接口自动化测试')
class TestCase:
    httpclient=HttpClient()
    openid=None
    proid=None
    userid=None
    cartid=None
    # 从yaml文件中获取数据传到代码里面  数据从yaml文件中取出来

    # 响应 token号会变 1.响应回来的token号提取出来 保存在变量。
    # 2.放在一个地方 都可以拿到token  类变量  其他方式 2.session  3.返回值
    # 作业：获得token   后面两条用例自己补充完
    # @allure.story('登录流程')
    # @allure.title('登录')
    @pytest.mark.parametrize('userdata',YamlUtil('./data/login.yml').read_yaml())
    def test_login(self,userdata):
        url=userdata['request']['url']
        # 张三 token 2h
        data=userdata['data']
        method=userdata['request']['method']
        param_type = userdata['request']['param_type']
        exmsg = userdata['exmsg']
        # res=requests.post(url,json=data)
        res=TestCase.httpclient(method=method,url=url,param_type=param_type,data=data)
        print(res.json())
        # 提取token  保存在变量中了  接口关联  要用的数据 提取出来 保存在变量中  类变量中 下个接口要用
        token=jsonpath.jsonpath(res.json(), '$..token')[0]
        # 把这个token放在session的headers里面  给头部里面设置属性 用update
        TestCase.httpclient.session.headers.update({'token':token})
        sjmsg=jsonpath.jsonpath(res.json(),'$..msg')[0]
        assert exmsg==sjmsg

    # # 获得个人信息  获得谁的个人信息  拿到token
    # # # # 注意 添加购物车 下单的时候需要用到这里面的userid和openid 这个怎么弄
    # @allure.story('获得个人信息流程')
    # @allure.title('个人信息')
    # 代码是调通 没有返回结果  你有没有取到数据  打印有没有数据
    @pytest.mark.parametrize('userdata', YamlUtil('./data/getUserInfo.yml').read_yaml())
    def test_getUserinfo(self,userdata):
        url=userdata['request']['url']
        method = userdata['request']['method']
        param_type = userdata['request']['param_type']
        exmsg = userdata['exmsg']
        res=TestCase.httpclient(url=url,method=method,param_type=param_type)
        # 获取所有的结果
        print(res.json())
        # userid和openid  jsonpath  字典取值 jsonpath(数据，表达式)
        TestCase.openid=jsonpath.jsonpath(res.json(),'$..openid')[0]
        TestCase.userid=jsonpath.jsonpath(res.json(),'$..userid')[0]
        # 出现问题  分析问题   没有取到值 直接报错  刚开始的代码都是调通 新加的代码 排查问题
        # print('useridfefefefefe',TestCase.userid)
        # print('openidfefeeffeef',TestCase.openid)
        sjname=jsonpath.jsonpath(res.json(),'$..nikename')[0]
        assert exmsg==sjname
    # # #  断言 取的数据 yaml里面的预期结果  可不可以和数据库里面的数据去进行对比？
    # 发请求之前 写好了链接数据库 调用数据库的增删改的函数  查询sql  返回的结果
    # # # # 选择商品 data=str  写法str  表单和json
    # @allure.story('选择商品流程')
    # @allure.title('商品')
    @pytest.mark.parametrize('userdata', YamlUtil('./data/getshopping.yml').read_yaml())
    def test_shopping(self,userdata):
        url = userdata['request']['url']
        method = userdata['request']['method']
        param_type = userdata['request']['param_type']
        exmsg = userdata['exmsg']
        res=TestCase.httpclient(url=url,method=method,param_type=param_type)
        print(res.json())
        TestCase.proid=jsonpath.jsonpath(res.json(),'$..productid')[0]
        sjproductid=jsonpath.jsonpath(res.json(),'$..productid')[0]
        assert exmsg==sjproductid
    # # #
    # # # # 添加购物车  为什么会失败  写法看着没有问题  注意  有问题  运行起来  没问题  没有运行起来
    # # # # 信息传入不正确 值 有问题  请求头  没有问题  没有测试 参数有没有问题  传的值对不对
    # # # # 确定一下 这个值是不是你想要 影响到你的判断 没有关联的代码注释掉
    # # # # 更好的解决代码  理解这一块步骤  你写的代码是什么意思
    # @allure.story('添加购物车流程')
    # @allure.title('购物车')
    # 可不可以把读取userid和openid写入到yaml文件中在读取出来  课后作业
    @pytest.mark.parametrize('userdata', YamlUtil('./data/getCart.yml').read_yaml())
    def test_cart(self,userdata):
        url = userdata['request']['url']
        method = userdata['request']['method']
        param_type = userdata['request']['param_type']
        userdata['data']['openid']=TestCase.openid
        userdata['data']['productid']=TestCase.proid
        userdata['data']['userid']=TestCase.userid
        data=userdata['data']
        exmsg = userdata['exmsg']
        # 参数 不能直接写死 userid  openid 取userid的值  取openid值 拿 哪里响应的哪个地方拿
        # userid和openid拿到值了  还是报错
        # res=requests.post(url,json=data,headers=header)
        res=TestCase.httpclient(url=url,method=method,param_type=param_type,data=data)
        print(res.json())
        TestCase.cartid = jsonpath.jsonpath(res.json(), '$..cartid')[0]
        # 断言  debug用在跳页面的时候  习惯
        sjmsg=jsonpath.jsonpath(res.json(),'$..cartid')[0]
        # print(sjmsg)
        assert exmsg==sjmsg
    #
    # @allure.story('下单流程')
    # @allure.title('下单')
    # def test_order(self):
    #     url='http://39.98.138.157:5000/api/createorder'
    #     data={ "cartid": TestCase.cartid, "openid": TestCase.openid, "productid": TestCase.proid, "userid": TestCase.userid}
    #     # res = requests.post(url, json=data, headers=header)
    #     res=TestCase.httpclient(url=url,method='post', data=data,param_type='json')
    #     print(res.json())

if __name__ == '__main__':
    pytest.main(['-sv','test_py4.py'])

# 流程 改变的地方
# get  post  一种方式 又能接受get又能接受post请求   封装 请求方式

# allure测试报告  漂亮的测试报告
# 出现问题 自己解决 打断点  大概的分析问题

# 作业：自己封装了request在给个测试报告

