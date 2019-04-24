"""
author songjie
"""
from googletrans import Translator


class Translate(object):
    def __init__(self):
        self.translator = Translator(service_urls=['translate.google.cn'])

    def translate(self, content, origin_language, aim_language):
        """
        :param content:
        :param origin_language:
        :param aim_language:
        :return:
        """
        data = self.translator.translate(content, src=origin_language, dest=aim_language).text
        return data
