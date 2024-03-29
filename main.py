
from config import load_config

if __name__ == '__main__':
    conf = load_config("config")
    # support "wechat" and "dingtalk" chat type.
    if conf['chat'] == "wechat":
        from app.wechat.wechat_channel import WechatChannel
        WechatChannel.startup()
        print("load wechat")
    elif conf['chat'] == "dingtalk":
        print("load dingtalk")
        # from app.dingtalk import application
        # application.run()
