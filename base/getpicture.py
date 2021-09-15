# -*- coding: utf-8 -*-
# @Author: 一凡

from selenium import webdriver
from base.readconfig import Config



class GetPicture():

    driver = webdriver.Chrome()

    def picture(self):
        self.driver.get_screenshot_as_file("baidu.png")

GP = GetPicture()
GP.picture()

