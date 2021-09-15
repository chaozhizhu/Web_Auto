# -*- coding: utf-8 -*-
# @Author: 一凡

import os
from base.readconfig import Config


class NewReport():

    """获取最新的测试报告"""
    path =  Config.BasePath + "\\report\\"
    # print(path)
    def report(self):
        # 获取文件夹中所有的文件(名)，以列表形式返回
        lists = os.listdir(self.path)
        #print("未经处理的文件夹列表：\n %s \n"%lists )
        # 按照key的关键字进行生序排列，lambda入参x作为lists列表的元素，获取文件最后的修改日期，
        # 最后对lists以文件时间从小到大排序
        lists.sort(key=lambda x:os.path.getmtime((self.path+x)))
        # 获取最新文件的绝对路径，列表中最后一个值,文件夹+文件名
        new_report = os.path.join(self.path, lists[-1])
        # print("时间排序后的的文件夹列表：\n %s \n"%lists )
        # print("最新文件路径:\n%s"%file)
        return new_report

# n = NewReport()
# print(n.report())
