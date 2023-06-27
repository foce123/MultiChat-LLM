import json
from utils.log import logger
import os
import pickle

class Config:
    def __init__(self):
        self.userdata = {}
        self.chat_conf = {}
        self.bot_conf = {}

    def read_file(path):
        try:
            with open(path, mode="r", encoding="utf-8") as f:
                data = json.loads(f)
                return data
        except FileNotFoundError as e:
            logger.error("[ERROR] config file: {} not exist!!!".format(path))

    def load_config(self):
        configPath = "./config.json"
        app_configPath = "./config/app-config.json"
        bot_configPath = "./config/bot-config.json"
        agent_configPath = "/config/agent-config.json"
        config = self.read_file(configPath)
        app_conf = self.read_file(app_configPath)
        if config['chat'] == "wechat":
            self.chat_conf = app_conf["wechat"]
        elif config['chat'] == "dingtalk":
            self.chat_conf = app_conf["dingtalk"]

        if config["chatbot"]:
            self.bot_conf = self.read_file(bot_configPath)
