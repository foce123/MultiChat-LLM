import json
from utils.log import logger
import os
import pickle

userdata = {}
chat_conf = {}
bot_conf = {}


def read_file(path) -> dict:
    try:
        with open(path, mode="r", encoding="utf-8") as f:
            data = json.load(f)
        return data
    except FileNotFoundError as e:
        logger.error("[ERROR] configs file: {} not exist!!!".format(path))


def load_config(conf_name):
    global chat_conf, bot_conf
    datas = {}
    cur_dir = os.path.dirname(os.path.abspath(__file__))
    pkl_path = os.path.join(cur_dir, "datas.pkl")
    configPath = "config.json"
    app_configPath = "./configs/app-config.json"
    bot_configPath = "./configs/bot-config.json"
    agent_configPath = "/configs/agent-config.json"
    if os.path.exists(pkl_path):
        with open(pkl_path, "rb") as f:
            datas = pickle.load(f)
    else:
        datas["config"] = read_file(configPath)
        datas["app_config"] = read_file(app_configPath)
        datas["bot_config"] = read_file(bot_configPath)
        datas["agent_config"] = read_file(agent_configPath)
        with open(pkl_path, "wb") as f:
            pickle.dump(datas, f)
    if conf_name == "config":
        return datas["config"]
    elif conf_name == "app_config":
        return datas["app_config"]
    elif conf_name == "bot_config":
        return datas["bot_config"]
    elif conf_name == "agent_config":
        return datas["agent_config"]
    else:
        logger.error("[ERROR] config file not exist!!!")
        os.error("config file not exist!!!")

    # app_conf = read_file(app_configPath)
    #
    # if config['chat'] == "wechat":
    #     chat_conf = app_conf["wechat"]
    # elif config['chat'] == "dingtalk":
    #     chat_conf = app_conf["dingtalk"]
    #
    # if config["chatbot"]:
    #     bot_conf = read_file(bot_configPath)


