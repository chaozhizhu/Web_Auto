# -*- coding: utf-8 -*-
# @Author: 一凡


from selenium.webdriver.common.by import By
from base.initbrowser import InitBrowser


class LoginPage(InitBrowser):
    """
    1、pages文件封装当前页面的元素指方法
    """

    # 登录首页的登录按钮
    home_login_button = (By.XPATH, '//*[text()="登录" and contains(@class, "am-btn-primary btn am-fl")]')
    user_input = (By.NAME, "accounts")
    pwd_input = (By.NAME, "pwd")
    login_button = (By.XPATH, '//*[text()="登录" and contains(@type, "submit")]')



    def login(self):
        """
        1、封装登录方法
        2、调用浏览器类中的自定义方法
        """
        self.my_click(LoginPage.home_login_button)
        self.my_send_keys(LoginPage.user_input, "zhichao")
        self.my_send_keys(LoginPage.pwd_input, "123456")
        self.my_click(LoginPage.login_button)
