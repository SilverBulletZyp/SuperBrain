# -*- coding: utf-8 -*-

"""

    baidu ocr

"""

from aip import AipOcr

def get_text_from_image_baidu(image_data):

    app_id = "10689123"
    app_key = "6QhomGENaVlR2sFgalNnlmbT"
    app_secret = "3h48wAGQY1hMde0s2fADDlmqfxhSjHPT"

    timeout = 3
    api_version = 0  # 0 表示普通识别, 1 表示精确识别

    client = AipOcr(appId=app_id, apiKey=app_key, secretKey=app_secret)
    client.setConnectionTimeoutInMillis(timeout * 1000)

    options = {}
    options["language_type"] = "CHN_ENG"

    if api_version == 1:
        result = client.basicAccurate(image_data, options)
    else:
        result = client.basicGeneral(image_data, options)

    if "error_code" in result:
        print("百度OCR识别出错，result" + result)
        return ""
    return [words["words"] for words in result["words_result"]]


