import requests
import json
from py11 import Mylogger
my_logger=Mylogger()
# class Runmain:
#     def __init__(self,url,method,data=None):
#         self.res = self.run_mian(url,method,data)
#
#     def send_get(self,url, data):
#         res1 = requests.get(url=url, data=data, verify=False)
#         # return json,dumps(res,indent=2,sort_keys=True)
#         return res1.content.decode()
#         # print(send_get(url,data))
#
#     def send_post(self,url, data):
#         res1 = requests.post(url=url, data=data).json()
#         # return json,dumps(res,indent=2,sort_keys=True)
#         return res1.content.decode()
#         # print(send_post(url,data))
#
#     def run_mian(self,url, method, data=None):
#         res = None
#         if method == 'GET':
#             res = self.send_get(url, data)
#         else:
#             res = self.send_post(url, data)
#         return res
# if __name__ == '__main__':
#
#     url = 'https://coding.imooc.com/class/ajaxsearchwords?callback=searchKeys&_=1567495525625'
#     data = {
#         'url': 'https://coding.imooc.com/',
#         'platform': '3',
#         'callback': 'callback11225645330078371',
#         'app_key': 'f375fe2f71e542a4b890d9a620f9fb32',
#     }
#     run = Runmain(url, 'GET', data)
#     print(run.res)
#     # print(run.run_mian(url, 'GET', data))

class HttpRequest:
    '''利用request封装get请求'''
    @staticmethod
    
    
    def http_request(url,data,method=None,cookie=None):
        try:
            if method== 'get':   # if method.lower() == 'get':    转换全部为小写
                res=requests.get(url,data,cookies=cookie)
                # return res
            elif method == 'post':  # if method.lower() == 'get':    转换全部为小写
                res = requests.post(url, data,cookies=cookie)
                # return res
            else:
                my_logger.info("输入的请求方式不对")
        except Exception as e:
            my_logger.error("请求出错了:{0}",format(e))
            raise e
            # print(res)
            # print("响应正文:", res.text)  # 字典类型的  只有json类型的才会有返回值
         #返回消息实体
        return res


