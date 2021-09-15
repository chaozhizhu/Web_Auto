# -*- coding: utf-8 -*-
# @Author: 一凡

import yaml
from base.readconfig import Config

class Yaml():

    def read_yaml(self):
        # 定义yaml文件路径
        yaml_path = Config.yaml_path
        # print(yaml_path)
        # 打开yaml文件
        file = open(yaml_path, "r", encoding="utf-8")
        # 读取
        string = file.read()
        dict = yaml.load(string, Loader=yaml.FullLoader)
        return dict

yaml_object = Yaml()
print(yaml_object.read_yaml())
url = yaml_object.read_yaml()["url"]["test_url"]
print(url)