import project_path
import pandas as pd
from read_config import ReadConfig
class GetCookie:
    check_list=eval(ReadConfig().get_config(project_path.case_config_path,'CHECKLEAVEAMOUNT','check_list'))
    Cookie=None
    loanId=None
    NoRegTel=pd.read_excel(project_path.test_case_path,sheet_name="init").iloc[0,0]
    #参照init表单查看我们这个变量的用处
    normal_tel=pd.read_excel(project_path.test_case_path,sheet_name="init").iloc[1,0]
    admin_tel=pd.read_excel(project_path.test_case_path,sheet_name="init").iloc[2,0]
    loan_member_id=pd.read_excel(project_path.test_case_path,sheet_name="init").iloc[3,0]




# setattr(GetCookie,'Cookie','12344')#设置属性值
# print(hasattr(GetCookie,'Cookie'))#判断是否有这个属性值
# delattr(GetCookie,'Cookie')
# print(hasattr(GetCookie,'Cookie'))#判断是否有这个属性值

# print(getattr(GetCookie,'Cookie'))  #获取属性值
# print(getattr(GetCookie,"NoRegTel"))

print(GetCookie.loan_member_id)

