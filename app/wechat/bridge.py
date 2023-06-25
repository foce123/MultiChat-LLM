
from common.context import Context
from common.reply import Reply
from utils.log import logger
from config import conf


def create_bot(bot_type):
    """
    create a bot_type instance
    :param bot_type: bot type code
    :return: bot instance
    """
    if bot_type == "baidu":
        # Baidu Unit对话接口
        from chatbot.baidu.baidu_unit_chat import BaiduUnitBot
        return BaiduUnitBot()
    # elif bot_type == "chatGPT":
    #     # ChatGPT 网页端web接口
    #     from chatbot.chatgpt.chat_gpt_bot import ChatGPTBot
    #     return ChatGPTBot()

    elif bot_type == "openAI":
        # OpenAI 官方对话模型API
        from chatbot.openai.openai_bot import OpenAIBot
        return OpenAIBot()
    # elif bot_type == "chatGPTAzure":
    #     # Azure chatgpt service https://azure.microsoft.com/en-in/products/cognitive-services/openai-service/
    #     from chatbot.chatgpt.chat_gpt_bot import AzureChatGPTBot
    #     return AzureChatGPTBot()

    elif bot_type == "linkai":
        from chatbot.linkai.linkai_bot import LinkAIBot
        return LinkAIBot()

    raise RuntimeError


# @singleton
class Bridge(object):
    def __init__(self):
        self.btype = {
            "chat": "openAI",
            "voice_to_text": conf().get("voice_to_text", "openai"),
            "text_to_voice": conf().get("text_to_voice", "google"),
            "translate": conf().get("translate", "baidu"),
        }
        model_type = conf().get("model")
        if model_type in ["text-davinci-003"]:
            self.btype["chat"] = "openAI"
        if conf().get("use_azure_chatgpt", False):
            self.btype["chat"] = "chatGPTAzure"
        if conf().get("use_linkai") and conf().get("linkai_api_key"):
            self.btype["chat"] = "linkai"
        self.bots = {}

    def get_bot(self, typename):
        if self.bots.get(typename) is None:
            logger.info("create bot {} for {}".format(self.btype[typename], typename))
            if typename == "text_to_voice":
                from agent.voice.google.google_voice import GoogleVoice
                self.bots[typename] = GoogleVoice()
            elif typename == "voice_to_text":
                from agent.voice.openai.openai_voice import OpenaiVoice
                self.bots[typename] = OpenaiVoice()
            elif typename == "chat":
                from chatbot.openai.openai_bot import OpenAIBot
                self.bots[typename] = OpenAIBot()
            elif typename == "translate":
                from agent.translate.baidu import BaiduTranslator
                self.bots[typename] = BaiduTranslator()
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