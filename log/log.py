# -*- coding: utf-8 -*-
# @Author: 一凡

import logging


class Log():

    def __init__(self, level="DEBUG"):
        """创建日志器"""

        self.log = logging.getLogger("一诺教育")
        self.log.setLevel(level)

    def console_handle(self, level="DEBUG"):
        """控制台处理器"""

        self.console_handler = logging.StreamHandler()
        # 设置控制台日志的等级
        self.console_handler.setLevel(level)
        # 处理器添加格式器
        self.console_handler.setFormatter(self.get_formatter()[0])
        return self.console_handler

    def file_handle(self, level="DEBUG"):
        """文件处理器"""

        self.file_handler = logging.FileHandler("./log.txt", mode="a", encoding="utf-8")
        # 设置文件处理器等级
        self.file_handler.setLevel(level)
        # 处理器添加格式器
        self.file_handler.setFormatter(self.get_formatter()[1])
        return self.file_handler

    def get_formatter(self):
        """格式器"""

        # 定义输出格式
        self.console_fmt = logging.Formatter(fmt="%(name)s--->%(levelname)s--->%(asctime)s--->%(message)s")
        self.file_fmt = logging.Formatter(fmt="%(levelname)s--->%(asctime)s--->%(message)s")
        return self.console_fmt, self.file_fmt

    def get_log(self):
        """日志器添加处理器和文件处理器"""

        # 日志器添加控制台处理器
        self.log.addHandler(self.console_handle())
        # 日志器添加文件处理器
        self.log.addHandler(self.file_handle())
        return self.log

# # 实列化日志类
# log = Log()
# a = log.get_log()
# a.debug("开始打印")
