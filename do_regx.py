__author__="zz"

import  re
from get_data import GetCookie

# s='www.lscns.com'  #目标字符串
# res=re.match('(w)(ww)',s)#全匹配  头部匹配
# print(res.group(0)) #group()==group(0) 拿到匹配的全字符  分组  根据你正则表达式里面的数字 框号里面是1就是第一组  是2就是第二组


# s='hellolemonfixlemon'
# res=re.findall('(le)(mon)',s)#列表 在字符串里面找  匹配的内容 存在列表里面
# #如果有分组 就是咦元组的形式表现出来  列表嵌套 元组·
# print(res)
class DoRegs:
    @staticmethod
    def do_regs(s):

        while re.search('\$\{(.*?)\}',s):  #r如果为真就true
            key=re.search('\$\{(.*?)\}',s).group(0)
            value=re.search('\$\{(.*?)\}',s).group(1)
            s=s.replace(key,str(getattr(GetCookie,value)))
            # print(key,value)
            # print(s)
        return s
if __name__ == '__main__':
    s = '{"mobilephone":"${admin_tel}","pwd":"${loan_member_id}"}'
    res=DoRegs.do_regs(s)
    print(res)
