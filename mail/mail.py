# -*- coding: utf-8 -*-
# @Author: 一凡

import zmail

from base.readyaml import Yaml
from base.readreport import NewReport
from log.log import Log


class Mail(NewReport, Yaml):

    """获取最新测试报告"""
    report_path = NewReport().report()
    # print(report_path)
    # 实例化yaml文件对像
    yaml = Yaml().read_yaml()
    # 分别取yaml文件内的值
    send_mail = yaml["mail"]["send_mail"]
    receive_mail = yaml["mail"]["receive_mail"]
    mail_code = yaml["mail"]["mail_code"]
    cc = yaml["mail"]["cc"]


    def mail(self):
        """发送邮件"""

        mail = {
            "subject": 'web自动化测试报告',
            "content_html":'报告详情请查看附件',
            "attachments": self.report_path
        }

        server = zmail.server(self.send_mail, self.mail_code)
        # 如果有多个收件人，则用列表
        server.send_mail(self.receive_mail, mail, Mail.cc)

# Mail = Mail()
# Mail.mail()