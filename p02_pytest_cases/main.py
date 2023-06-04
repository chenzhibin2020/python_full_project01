# -*- coding: utf-8 -*-
"""
@File    : main.py
@Author  : chenzhibin
@Time    : 2023/5/26 13:58
"""
import os

import pytest
import pipreqs

# 程序说明:
# 程序结果: 是否报错：xx，是否拿到结果：xx

if __name__ == '__main__':
    pytest.main(['-s', '--alluredir', './allure_result', '--clean-alluredir'])
    print("things done !")
    # # os.system('allure generate ./allure_result -o ./allure_report --clean')
    # os.system('pip freeze >depends.txt')
