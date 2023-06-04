# -*- coding: utf-8 -*-
"""
@File    : keywords_class.py
@Author  : chenzhibin
@Time    : 2023/5/26 13:42
"""
import allure
import jsonpath
import requests


# 程序说明:
# 程序结果: 是否报错：xx，是否拿到结果：xx

class Key_words():

    # 封装get请求
    @allure.step("发送get请求")
    def get(self, url, params=None, **kwargs):
        resp = requests.get(url, params=params, **kwargs)
        return resp

    # 封装post请求
    @allure.step("发送post请求")
    def post(self, url, data=None, json=None, **kwargs):
        resp = requests.post(url=url, data=data, json=json, **kwargs)
        return resp

    # 获取应答报文的对应字段
    @allure.step("报文解析")
    def get_text(self, resp, json_path):
        self.resp = resp
        text = jsonpath.jsonpath(resp, json_path)
        return text


if __name__ == '__main__':
    login_url = "http://shop-xo.hctestedu.com/index.php?s=api/user/login"
    login_para = {"application": "app", "application_client_type": "weixin"}
    login_data = {"accounts": "chenzhibin", "pwd": "chc001", "type": "username"}
    kw = Key_words()
    print(kw.post(url=login_url, params=login_para, json=login_data).text)
