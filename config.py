import json
from utils.log import logger
import os

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
    configPath = "config.json"
    app_configPath = "./configs/app-config.json"
    bot_configPath = "./configs/bot-config.json"
    agent_configPath = "/configs/agent-config.json"
    if conf_name == "config":
        config = read_file(configPath)
        return config
    elif conf_name == "app_config":
        config = read_file(app_configPath)
        return config
    elif conf_name == "bot_config":
        config = read_file(bot_configPath)
        return config
    elif conf_name == "agent_config":
        config = read_file(agent_configPath)
        return config
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


