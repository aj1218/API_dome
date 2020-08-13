
import logging   #python 字典   日志在输入的时候要经过两个门槛
#第一个门槛:logge收集日志 debug  info  error
#第二个门槛: haddler 输出的日志渠道 指定文件 还是控制台  默认到控制台
#
# logging.debug("这是一个debug信息")
# logging.info("这是一个info的信息")
# logging.warning("这是一个warning的信息")
# logging.error("这是一个error的信息")
# logging.critical("这是一个critical的信息")
#定义一个日志收集器
class Mylogger:
    def my_logger(self,msg,level):
        my_logger=logging.getLogger("python11")

        #设定级别
        my_logger.setLevel("DEBUG")

        #设置输出格式
        formatter=logging.Formatter('%(asctime)s-%(levelname)s-%(filename)s-%(lineno)s-%(name)s-日志信息:%(message)s')

        #创建一个自己的输出渠道
        logging.basicConfig(level=logging.INFO)
        ch=logging.StreamHandler(stream=None) #设置输出渠道 控制台
        ch.setLevel("DEBUG")
        ch.setFormatter(formatter)

        fh=logging.FileHandler("py11.txt",encoding='UTF-8') #写入文件里面的时候,在对戒的时候一点要对接一下 不然数据写入失败
        fh.setLevel("DEBUG")  #文件输出渠道
        fh.setFormatter(formatter)

        #两者对接   -----指定输出渠道
        my_logger.addHandler(ch)#控制台
        my_logger.addHandler(fh)#文件

        #收集日志
        if level=="DEBUG":
            my_logger.debug(msg)
        elif level=="INFO":
            my_logger.error(msg)
        elif level == "WARNING":
            my_logger.error(msg)
        elif level=="ERROR":
            my_logger.error(msg)
        elif level=="CTITICAL":
            my_logger.error(msg)

        #关闭日志收集器渠道
        my_logger.removeHandler(ch)
        my_logger.removeHandler(fh)


    def debug(self,msg):
        self.my_logger(msg,"DEBUG")
    def info(self,msg):
        self.my_logger(msg,"INFO")
    def error(self,msg):
        self.my_logger(msg,"ERROR")

if __name__ == '__main__':
    # Mylogger().my_logger("不次哦啊USB粗搜查吧","ERROR")
    # Mylogger().my_logger("说清楚我欺负我出去玩","ERROR")
    test=Mylogger()
    test.debug("ceececece")
    test.info("xssxs")

