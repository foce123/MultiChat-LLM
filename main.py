
from config import *

if __name__ == '__main__':
    if chat_conf.name == "wechat":
        pass
    elif chat_conf.name == "dingtalk":
        from app.dingtalk import application
        application.run()
