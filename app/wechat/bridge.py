
from common.context import Context
from common.reply import Reply
from utils.log import logger
# from common.singleton import singleton
from config import conf
from translate.factory import create_translator
from agent.voice.factory import create_voice


def create_bot(bot_type):
    """
    create a bot_type instance
    :param bot_type: bot type code
    :return: bot instance
    """
    if bot_type == "baidu":
        # Baidu Unit对话接口
        from chatbot.baidu.baidu_unit_bot import BaiduUnitBot
        return BaiduUnitBot()

    elif bot_type == "chatGPT":
        # ChatGPT 网页端web接口
        from chatbot.chatgpt.chat_gpt_bot import ChatGPTBot
        return ChatGPTBot()

    elif bot_type == "openAI":
        # OpenAI 官方对话模型API
        from chatbot.openai.open_ai_bot import OpenAIBot
        return OpenAIBot()

    elif bot_type == chatGPTAzure:
        # Azure chatgpt service https://azure.microsoft.com/en-in/products/cognitive-services/openai-service/
        from chatbot.chatgpt.chat_gpt_bot import AzureChatGPTBot
        return AzureChatGPTBot()

    elif bot_type == "linkai":
        from chatbot.linkai.link_ai_bot import LinkAIBot
        return LinkAIBot()

    raise RuntimeError


# @singleton
class Bridge(object):
    def __init__(self):
        self.btype = {
            "chat": const.CHATGPT,
            "voice_to_text": conf().get("voice_to_text", "openai"),
            "text_to_voice": conf().get("text_to_voice", "google"),
            "translate": conf().get("translate", "baidu"),
        }
        model_type = conf().get("model")
        if model_type in ["text-davinci-003"]:
            self.btype["chat"] = const.OPEN_AI
        if conf().get("use_azure_chatgpt", False):
            self.btype["chat"] = const.CHATGPTONAZURE
        if conf().get("use_linkai") and conf().get("linkai_api_key"):
            self.btype["chat"] = const.LINKAI
        self.bots = {}

    def get_bot(self, typename):
        if self.bots.get(typename) is None:
            logger.info("create bot {} for {}".format(self.btype[typename], typename))
            if typename == "text_to_voice":
                self.bots[typename] = create_voice(self.btype[typename])
            elif typename == "voice_to_text":
                self.bots[typename] = create_voice(self.btype[typename])
            elif typename == "chat":
                self.bots[typename] = create_bot(self.btype[typename])
            elif typename == "translate":
                self.bots[typename] = create_translator(self.btype[typename])
        return self.bots[typename]

    def get_bot_type(self, typename):
        return self.btype[typename]

    def fetch_reply_content(self, query, context: Context) -> Reply:
        return self.get_bot("chat").reply(query, context)

    def fetch_voice_to_text(self, voiceFile) -> Reply:
        return self.get_bot("voice_to_text").voiceToText(voiceFile)

    def fetch_text_to_voice(self, text) -> Reply:
        return self.get_bot("text_to_voice").textToVoice(text)

    def fetch_translate(self, text, from_lang="", to_lang="en") -> Reply:
        return self.get_bot("translate").translate(text, from_lang, to_lang)