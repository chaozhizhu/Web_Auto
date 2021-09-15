# -*- coding: utf-8 -*-
# @Author: 一凡

import os

class Config():

    # E:\test
    BasePath = os.path.abspath(os.path.dirname(__file__) + "/..")
    # print(BasePath)
    report_path = BasePath + r"\report"
    yaml_path = BasePath + "\\config\\yaml.yaml"
    picture_path = BasePath + "\\picture\\"

# print(Config())
import os

