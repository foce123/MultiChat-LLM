
from config import load_config

if __name__ == '__main__':
    conf = load_config("config")
    print(conf['chat'])
    # if chat_conf.name == "wechat":
    #     pass
    # elif chat_conf.name == "dingtalk":
    #     print("dingtalk")
        # from app.dingtalk import application
        # application.run()
