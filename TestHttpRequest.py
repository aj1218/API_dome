import unittest
from demo import HttpRequest
from get_data import GetCookie
from ddt import ddt,data
from do_Excel import Doexcel
import project_path
from py11 import Mylogger
from do_mysql import DoMysql
from get_data import GetCookie
# import pdb

my_logger=Mylogger()
test_data=Doexcel.get_excel(project_path.test_case_path)#执行所有的用例
# test_data={"case_id":"1","url":"http://120.78.128.25:8765/Index/login","data":'{"mobilephone": "${normal_tel}","pwd": "123456","amount":1000}',
#            'check_sql':'{"sql":"select * from member where MobilePhone=${normal_tel}"}','expected':'10010','method':'post','title':'111'}
@ddt
class TestHttptest(unittest.TestCase):

    def setUp(self):
        my_logger.info('开始测试啦!')


    @data(*test_data)
    def test_001(self,item):
        # url = "http://120.78.128.25:8765/Index/login"
        # data = {
        #     "mobilephone": "15388030234", "pwd": "1231456"}
        #请求之前完成loanId的替换
        my_logger.info("开始执行用例{0}:{1}".format(item['case_id'],item['title']))
        my_logger.info(item)
        # pdb.set_trace()
        if item["data"].find('${loan_id}')!=-1:
            if getattr(GetCookie,'loanId')==None:  #判断是否有那个loanid如果没有直接从数据库里面查如果有直接使用
                query='select Id from loan where MemberID={0}'.format(getattr(GetCookie,"loan_member_id"))
                # pdb.set_trace()
                loan_id=DoMysql().do_mysql(query)[0][0] #拿到数据之后就要替换
                item['data']=item['data'].replace('${loan_id}',str(loan_id))
                setattr(GetCookie,'loanId',loan_id)#利用反射存数据结果
                my_logger.info(loan_id)

            else:
                my_logger.info(getattr(GetCookie,'loanId'))
                item['data'] = item['data'].replace('${loan_id}', str(getattr(GetCookie,'loanId')))
        #开始请求

        my_logger.info("获得的请求数据是{0}".format(item['title']))
        if item['check_sql']!=None: #当你的数据语句不为空的时候 就可以进行数据库校验
            my_logger.info("此条用例需要做到数据库校验:{0}".format(item['data']))
            sql=eval(item['check_sql'])['sql']  #拿到sql语句  是存在字典里面的(check_sql)
            #开始查询
            # 请求之前的账户余额
            try:
             Before_Amount1=DoMysql.do_mysql("select * from member where MobilePhone=13131313131",1)[0][0]#sql语句返回的是元祖  所以我们要加上[0]不然读不到
            except:
                Before_Amount1=""

            my_logger.info("用例:{0}请求之前的余额是{1}".format(item['title'],Before_Amount1))

            my_logger.info("-----------开始http接口请求-------------------")
            res=HttpRequest.http_request(item['url'],eval(item['data']),item['method'],getattr(GetCookie,'Cookie'))
            my_logger.info("-----------完成http接口请求-------------------")
            After_Amount = DoMysql().do_mysql(sql,1)#请求之后用户的余额
            my_logger.info("用例:{0}请求之前的余额是{1}".format(item['title'],After_Amount))

            #检查结果
            # if eval(item['data'])['amount']==After_Amount-Before_Amount1:
            #             #     my_logger.info('数据库校验通过')
            #             #     check_sql_result = '数据库检查通过'
            #             # else:
            #             #     my_logger.info('数据库校验未通过')
            classheck_sql_result = '数据库检查未通过'
            #怎么把结果写回  这里重新改写了Doexcel中的writeback方法
            Doexcel().write_back(project_path.test_case_path,item["sheet_name"],item['case_id']+1,10,classheck_sql_result)
        # if item['sheet_name'] in getattr(GetCookie,'check_list'):
        #     # 请求之前查询余额
        #     #查询数据库
        #     query_sql='select LeaveAmount from member where Moblilephone={0}'.format(eval(item['data'])['mobilephone'])
        #     Before_Amount=DoMysql().do_mysql(query_sql,1)[0]  #请求之前的账户余额
        #     res=HttpRequest.http_request(item['url'],eval(item['data']),item['method'],getattr(GetCookie,'Cookie'))
            # data={"mobilephone": "${normal_tel}","pwd": "123456","sql":"select * from member where MobliePhone=${normal_tel}"}
            # check_sql=data['check_sql']  #为啥要删因为在进行hppt请求的时候check_sql是不能进行请求的
            # data=data.pop("check_sql")#限于写在一起的时候不是分开写的


            #请求之后  校验余额 是否正确
            # query_sql1='select LeaveAmount from member where Moblilephone={0}'.format(eval(item['data'])['mobilephone'])
            # After_Amount = DoMysql().do_mysql(query_sql1, 1)[0]
            # if abs(Before_Amount-After_Amount)==eval(item['data'])['amount']:
            #     check_res='金额正确'
            # else:
            #     check_res='金额不正确'
            #     #并不是全部用例可以这么做! 怎么去解决这个问题  可否在数据库里面做或者在excel里面判断
            #     # 还会有其他的异常情况
            #     #怎么把数据库的检查结果写在Excel里面去
            #     #多个语句怎么分   如果要检查多个语句要怎么办

        else:
            my_logger.info("此条用例不需要做到数据库校验:{0}".format(item['data']))
            my_logger.info("-----------开始http接口请求-------------------")
            res=HttpRequest.http_request(item['url'],eval(item['data']),item['method'],getattr(GetCookie,'Cookie'))
            my_logger.info("-----------完成http接口请求-------------------")


        if res.cookies:
            getattr(GetCookie, 'Cookie',res.cookies) #把cokies写回去  不然用例执行失败  利用反射存cookies 登录的时候一定要写
        #结果过不过在断言那里可以体验出来
        try:
            self.assertEqual(str(item['expected']),res.text)
            TestResult="PASS"  #成功
        except AssertionError as e:
            TestResult = "Failed"   #失败
            my_logger.info("执行用例出错：{0}".format(e))
            raise e
        finally:   #y执行用例的时候如果是Failed excel中将不写入失败的结果 加上finally的时候失败和成功的都可以写入
            Doexcel().write_back(project_path.test_case_path,item["sheet_name"],item['case_id']+1,8,str(res.text))
            Doexcel().write_back(project_path.test_case_path,item["sheet_name"],item['case_id']+1,9,TestResult)

            my_logger.error("获取到的结果是：{0}".format(res.text))
    def tearDown(self):
        my_logger.info('我结束测试了')


if __name__ == '__main__':
    unittest.main()
