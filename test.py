# from base.demo import Runmain
#
# class TestMethod(unittest.TestCase):
#
#     # @classmethod
#     # def setUpClass(cls):
#     #     print('类执行之前的方法')
#     #
#     # @classmethod
#     # def tearDownClas(cls):
#     #     print('类执行之后的方法')
#     #  # 每次方法之前执行
#     # def setUp(self) -> None:
#     #     print('test--------setup')
#     # # 每次方法之后执行
#     # def tearDown(self) -> None:
#     #     print('test-----tearDown')
#     def setUp(self,url, method, data) -> None:
#
#       self.res = Runmain.run_mian(url, method, data)
#
#
#     def test_01(self):
#         url='https://coding.imooc.com/class/ajaxsearchwords?callback=searchKeys&_=1567495525625'
#         data = {
#             'platform': '3',
#             'callback': 'callback11225645330078371',
#             'app_key': 'f375fe2f71e542a4b890d9a620f9fb32',
#         }
#
#         res = self.res(url,'GET',data)
#         print(res)
#         print('这是第一个测试方法')
#     # def test_02(self):
#     #     url = 'https://coding.imooc.com/class/ajaxsearchwords?callback=searchKeys&_=1567495525625'
#     #     data = {
#     #         'platform': '3',
#     #         'callback': 'callback11225645330078371',
#     #         'app_key': 'f375fe2f71e542a4b890d9a620f9fb32',
#     #     }
#     #     res = self.run.run_mian(url,'GET',data)
#     #     print(res)
#     #     print('这是第二个测试方法')
# if __name__ == '__main__':
#     unittest.main()
from demo import HttpRequest
from do_Excel import Doexcel
from get_data import GetCookie
# # test_data=[{"url":"http://120.78.128.25:8765/Index/login",
# #             "data":{"phone": "15388030234","password": "123456"},"title":"正常登陆","method":"get"},
# #             {"url":"http://120.78.128.25:8765/Index/login",
# #             "data":{"phone": "15388030234","password": "123456"},"title":"异常登陆","method":"post"}
# #            ]
# # COOLIE=None
# def run(test_data):
#     url = "http://120.78.128.25:8765/Index/login"
#     # data = {
#     #     "mobilephone": "15388030234","pwd": "123456"
#     #
#     # }
#     # global COOLIE
#     for item in test_data:
#         print("正在测试的用例是{0}".format(item["title"]))
#         res = HttpRequest().http_request(item['url'], item["data"], item["method"],getattr(GetCookie,'Cookie'))
#         if res.cookies: #非空和非零的数据布尔值都是true
#             # COOLIE=res.cookies
#             setattr(GetCookie,'Cookie',res.cookies)
#         print("请求的结果是{0}".format(res.text))
#         Doexcel().write_back(r"C:\Users\tangting\Desktop\test.xlsx","login",item["case_id"]+1,res.text)
#
#     # print("课堂派登录的结果是{0}".format(res))
#     # print("响应正文:", res.text)
# test_data=Doexcel().get_excel(r"C:\Users\tangting\Desktop\test.xlsx","login")
# run(test_data)
import unittest
import HTMLTestrunner
import project_path
from py11 import Mylogger
my_logger=Mylogger()
from TestHttpRequest import TestHttptest    #如果是 from tool.TestHttpRequest import TestHttptest   直接写成 from TestHttpRequest import TestHttpRequest
# from TestHttpRequesttest01 import TestHttptest   #因为他们两的名字是一样的  直接使用 文件名点方法名  不具体到里面的类名  然后下面读取用例从
#loadTestsFromTestCase 改成   loadTestsFromModule

suite=unittest.TestSuite()
# suite.addTest(TestHttptest("test_001"))#测试用例的实例
#执行用例
# runner=unittest.TextTestRunner()

# runner.run(suite)
loader=unittest.TestLoader()

#如果测试用例一个一个导入再别人跑你的用例的时候会烦死的
#最优解就是多个用例
suite.addTest(loader.loadTestsFromTestCase(TestHttptest))
with open(project_path.test_case_THML,"wb")as file:
    runner=HTMLTestrunner.HTMLTestRunner(stream=file, verbosity=2, title=None, description="这个是单元测试报告")
    my_logger.info('开始测试啦!')
    runner.run(suite)

