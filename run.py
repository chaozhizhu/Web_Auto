# -*- coding: utf-8 -*-
# @Author: 一凡

import unittest
import HTMLTestRunner
import time
from base.readconfig import Config
from mail.mail import Mail
from log.log import Log

class HC(unittest.TestCase, Config):

    pass

if __name__ == '__main__':
    log = Log()
    lg = log.get_log()
    lg.debug("开始执行")
    """定义文件路径和执行用例"""
    now_time = time.strftime("%Y %m-%d %H-%M")
    # 定义报告生成的路径
    report_path = Config.BasePath + "\\report\\"
    # 用例的路径
    test_path = Config.BasePath +"\\testcase"
    Html_file = open(report_path + now_time + ".html", "wb")
    # 用例加载
    lg.debug("执行用例中。。。。。。")
    dis = unittest.defaultTestLoader.discover(start_dir=test_path, pattern="test*.py")
    # 将测试数据写入到html文件
    run = HTMLTestRunner.HTMLTestRunner(Html_file, title="自动化测试报告", description="执行结果")
    # 运行用例
    run.run(dis)
    lg.debug("发送邮件")
    Mail = Mail()
    Mail.mail()
    lg.debug("关闭文件")
    Html_file.close()
    lg.debug("执行结束")
