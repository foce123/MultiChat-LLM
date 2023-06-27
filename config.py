import json
from utils.log import logger
from ast import literal_eval
import os

userdata = {}
chat_conf = {}
bot_conf = {}


def read_file(path):
    try:
        with open(path, mode="r", encoding="utf-8") as f:
            data = literal_eval(f)
            return data
    except FileNotFoundError as e:
        logger.error("[ERROR] configs file: {} not exist!!!".format(path))


def load_config():
    global chat_conf, bot_conf
    configPath = "./config.json"
    app_configPath = "./configs/app-config.json"
    bot_configPath = "./configs/bot-config.json"
    agent_configPath = "/configs/agent-config.json"
    config = read_file(configPath)
    app_conf = read_file(app_configPath)
    if config['chat'] == "wechat":
        chat_conf = app_conf["wechat"]
    elif config['chat'] == "dingtalk":
        chat_conf = app_conf["dingtalk"]

    if config["chatbot"]:
        bot_conf = read_file(bot_configPath)


load_config()
