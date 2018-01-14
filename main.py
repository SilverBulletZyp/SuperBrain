# -*- coding:utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from core.ocr import baiduocr
from core import windows







# def main():




if __name__ == "__main__":
    # main()


    # print("123")
    browser = webdriver.Chrome(r'.\tools\chromedriver.exe')
    browser.get("http://www.baidu.com")

    image1 = r'.\screenshots\TIM001.png'

    image = windows.get_area_data(image1)

    keyword = baiduocr.get_text_from_image_baidu(image_data=image)

    # print(keyword)

    elem = browser.find_element_by_id("kw")
    elem.clear()
    elem.send_keys(keyword)
    elem.send_keys(Keys.RETURN)


