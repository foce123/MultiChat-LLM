import json
from utils.log import logger
import os
import pickle

userdata = {}
chat_conf = {}
bot_conf = {}


class Config:
    def __init__(self):
        self.user_datas = {}

    def get_user_data(self, user) -> dict:
        if self.user_datas.get(user) is None:
            self.user_datas[user] = {}
        return self.user_datas[user]

    def load_user_datas(self):
        try:
            with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "user_datas.pkl"), "rb") as f:
                self.user_datas = pickle.load(f)
                logger.info("[Config] User datas loaded.")
        except FileNotFoundError as e:
            logger.info("[Config] User datas file not found, ignore.")
        except Exception as e:
            logger.info("[Config] User datas error: {}".format(e))
            self.user_datas = {}

    def save_user_datas(self):
        try:
            with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "user_datas.pkl"), "wb") as f:
                pickle.dump(self.user_datas, f)
                logger.info("[Config] User datas saved.")
        except Exception as e:
            logger.info("[Config] User datas error: {}".format(e))


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
    agent_configPath = "./configs/agent-config.json"
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



