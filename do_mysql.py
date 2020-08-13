

import mysql.connector
import project_path
from read_config import ReadConfig
from get_data import GetCookie
from py11 import Mylogger
from get_data import GetCookie
import pdb
my_logger=Mylogger()
# config=eval(ReadConfig.get_config(project_path.case_config_path,'DB','config'))#创建数据库连接
#
# cnn=mysql.connector.connect(**config) #关键字参数的传递
#
# #游标cursor
# cur = cnn.cursor(buffered = True)
# #写sql语句
# query_sql = "SELECT MobilePhone from member WHERE MobilePhone like'131%'"
#
# #执行语句
# cur.execute(query_sql)
#
# #打印结果
#
# res=cur.fetchall()
# print(res)
#
#
# #关闭游标
# cur.close()
#
# #关闭连接
#
# cnn.close()

# config={'host':'47.107.168.87',
#         'user':'python',
#         'password':'python666',
#         'database':'future',
# }#创建数据库连接
class DoMysql:
    @staticmethod
    def do_mysql(query,state='all'):
        db_config=eval(ReadConfig.get_config(project_path.case_config_path,'DB','config'))
        #利用这个类读取文件
        cnn = mysql.connector.connect(**db_config)

        cur = cnn.cursor(buffered = True)
        #执行语句
        cur.execute(query)
        if state==1:
            res = cur.fetchone()#数据库单l行
        else:
            res = cur.fetchall()#多行
        # print(int(res[0]+1))


        cur.close()
        cnn.close()
        return res
if __name__ == '__main__':
    
    query = 'select Id from loan where MemberID=42551 '
    pdb.set_trace()
    res=DoMysql().do_mysql(query)[0][0]
    res1=int(res)+1
    if int(1) == abs(res1 - res):
        my_logger.info('数据库校验通过')
        print('数据库检查通过')
    else:
       print('数据库校验未通过')
    # print(res[0][0])
    # print(res1)

