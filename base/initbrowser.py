# -*- coding: utf-8 -*-
# @Author: 一凡

from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from base.readconfig import Config


class InitBrowser():
    """
    封装公用的页面操作方法
    """

    def __init__(self, driver):
        self.driver = driver

    def wait_element(self, loc):
        """找元素，返回web element对像"""

        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(loc))
        return element

    def my_send_keys(self, loc, value):
        """自定义输入的方法"""

        self.wait_element(loc).send_keys(value)

    def my_click(self, loc):
        """自定义点击方法"""

        self.wait_element(loc).click()

    def get_picture(self, pic_name):
        """截图"""

        config = Config()
        self.driver.get_screenshot_as_file(config.picture_path + pic_name + ".png")



