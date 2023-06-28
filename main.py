
from config import load_config

if __name__ == '__main__':
    conf = load_config("config")
    if conf['chat'] == "wechat":
        pass
    elif conf['chat'] == "dingtalk":
        print("dingtalk")
        # from app.dingtalk import application
        # application.run()
