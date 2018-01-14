# -*- coding: utf-8 -*-

"""

    baidu ocr

"""

from aip import AipOcr
import configparser


def get_text_from_image_baidu(image_data):
    """
    Get image text use baidu ocr

    :param image_data:
    :param api_version:
    :param timeout:
    :return:
    """

    conf = configparser.ConfigParser()
    conf.read("config.ini")
    app_id = conf.get('config', "app_id")
    app_key = conf.get('config', "app_key")
    app_secret = conf.get('config', "app_secret")

    timeout = 3

    client = AipOcr(appId=app_id, apiKey=app_key, secretKey=app_secret)
    client.setConnectionTimeoutInMillis(timeout * 1000)

    options = {}
    options["language_type"] = "CHN_ENG"

    api_version = 0  # 0 表示普通识别, 1 表示精确识别

    if api_version == 1:
        result = client.basicAccurate(image_data, options)
    else:
        result = client.basicGeneral(image_data, options)

    if "error_code" in result:
        print("百度OCR识别出错，是不是免费使用次数用完了啊~")
        return ""
    return [words["words"] for words in result["words_result"]]


