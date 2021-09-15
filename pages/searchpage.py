# -*- coding: utf-8 -*-
# @Author: 一凡


from selenium.webdriver.common.by import By
from base.initbrowser import InitBrowser


class SearchPage(InitBrowser):

    search_input = (By.ID, "search-input")
    search_button = (By.ID, "ai-topsearch")


    def search(self, value):
        """
        1、封装search方法
        2、调用浏览器类中的自定义方法
        """
        self.my_send_keys(SearchPage.search_input, value)

    def click(self):
        """
        1、封装点击方法
        2、调用浏览器类中的自定义点击方法
        """
        self.my_click(SearchPage.search_button)