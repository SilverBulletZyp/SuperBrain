# -*- coding:utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from core.ocr import baiduocr
from core import windows





if __name__ == "__main__":

    browser = webdriver.Chrome(r'.\tools\chromedriver.exe')
    browser.get("http://www.baidu.com")

    imagePath = r'.\screenshots\TIM001.png'
    image = windows.get_area_data(imagePath)

    keyword = baiduocr.get_text_from_image_baidu(image)

    print(keyword)

    elem = browser.find_element_by_id("kw")
    elem.clear()
    elem.send_keys(keyword)
    elem.send_keys(Keys.RETURN)


