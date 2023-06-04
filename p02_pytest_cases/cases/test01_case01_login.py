# -*- coding: utf-8 -*-
"""
@File    : test01_case01_login.py
@Author  : chenzhibin
@Time    : 2023/5/26 13:13
"""
import allure
# 程序说明:  登陆华测商城的用例
# 程序结果: 是否报错：xx，是否拿到结果：xx


import jsonpath
import pytest
import requests
from p02_pytest_cases.keywords.keywords_class import Key_words


@allure.title("用户登录")
def test01_login():
    login_url = "http://shop-xo.hctestedu.com/index.php?s=api/user/login&application=app"
    login_para1 = {"application": "app", "application_client_type": "weixin"}
    login_data = {"accounts": "chenzhibin", "pwd": "chc001", "type": "username"}

    kw=Key_words()

    # 发送请求
    # login_url = url
    # login_para1 = params
    # login_data = data

    resp = kw.post(url=login_url, params=login_para1, json=login_data)
    print(resp.text)
    msg = kw.get_text(resp.json(), '$..msg')[0]
    print("msg:", msg)
    resp_token = jsonpath.jsonpath(resp.json(), '$..token')[0]
    print("resp_msg:", resp_token)
    return resp_token

if __name__ == '__main__':
    # pytest.main(['-s','test01_case01_login.py'])
    print(test01_login())