# -*- coding: utf-8 -*-
# @Author: 一凡

import unittest
from selenium import webdriver
from base.initbrowser import InitBrowser
from pages.loginpage import LoginPage
from base.readyaml import Yaml
from pages.loginpage import LoginPage
from pages.searchpage import SearchPage
from log.log import Log

class Test1(unittest.TestCase, Yaml, LoginPage, SearchPage):

    log = Log()
    lg = log.get_log()
    yaml_object = Yaml()
    url = yaml_object.read_yaml()["url"]["test_url"]

    @classmethod
    def setUpClass(self) -> None:
        """所有用例前置"""

        self.driver = webdriver.Chrome()
        self.driver.get(self.url)
        self.browser = InitBrowser(self.driver)

    def test1(self):
        """登录"""

        self.lg.debug("开始执行登录用例")
        self.driver.maximize_window()
        self.login()
        self.get_picture("登录")

    def test2(self):
        """搜索功能"""

        self.lg.debug("开始执行搜索用例")
        self.search("包包")
        self.click()
        self.get_picture("包包")

    @classmethod
    def tearDownClass(self) -> None:
        """所有用例后置"""
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()