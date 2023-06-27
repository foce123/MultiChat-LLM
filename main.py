
from config import Config

if __name__ == '__main__':
    conf = Config()
    if conf.chat_conf.name == "wechat":
        pass
    elif conf.chat_conf.name == "dingtalk":
        from app.dingtalk import application
        application.run()
