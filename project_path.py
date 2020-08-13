##用来获取路劲得值
import os
path=os.path.split(os.path.realpath(__file__))[0]
# test_case_path=os.path.join(path,'test_data.xlsx')
# print(test_case_path)
# path=os.path.realpath(__file__) #绝对路径
#os.path.split  切回上一级 记得加  [0]  切一次加一个[0]


#配置文件路径
case_config_path=os.path.join(path,'case.config')
print(case_config_path)

#登录的测试用例文件
test_case_path=os.path.join(path,'test.xlsx')

print(test_case_path)

#测试用例输出文件
test_case_THML=os.path.join(path,'test.html')
print(test_case_THML)

#日志的路劲
logger_path=os.path.join(path,'py11.txt')
# print(logger_path)
