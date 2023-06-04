# -*- coding: utf-8 -*-
"""
@File    : test01_case09_submit_order.py
@Author  : chenzhibin
@Time    : 2023/5/26 21:02
"""
import allure
# 程序说明: 提交订单程序。 提交订单涉及多个前置步骤。
# 程序结果: 是否报错：xx，是否拿到结果：xx


import jsonpath
import requests
from time import sleep
from p02_pytest_cases.keywords.keywords_class import Key_words
# DS_999 订单支付
@allure.title("订单支付")
def test09_submit_order():

    kw = Key_words()
    # 01 执行登陆获取token
    with allure.step("01 执行登陆获取token"):
        data = {
            "accounts": "chenzhibin",
            "pwd": "chc001",
            "type": "username"
        }

        params = {
            "application": "app",
            "application_client_type": "weixin",
        }
        r1 = kw.post(url="http://shop-xo.hctestedu.com/index.php?s=api/user/login", params=params, json=data)
        token_list = kw.get_text(r1.json(), '$..token')
        token = token_list[0]
        print("token :", token)

    # 02 加入购物车
    with allure.step("02 加入购物车"):
        print("02 加入购物车")
        data = {
            "goods_id": "10",
            "spec": "",
            "stock": 1
        }

        params = {
            "application": "app",
            "application_client_type": "weixin",
            "token": token
        }

        res = kw.post(url="http://shop-xo.hctestedu.com/index.php?s=api/cart/save", params=params, json=data)
        print(res.text)
        order_submit_msg = kw.get_text(res.json(), '$..msg')[0]
        assert order_submit_msg =='加入成功'



    # 03 查询购物车

    print("03 查询购物车")
    with allure.step("03 查询购物车"):
        params = {
            "application": "app",
            "application_client_type": "weixin",
            "token": token
        }
        res = kw.get(url="http://shop-xo.hctestedu.com/index.php?s=api/cart/index", params=params, json=data)
        print(res.text)
        # 获取购物车id
        cartid_list = kw.get_text(res.json(),'$..id')
        cartid = cartid_list[0]
        print("cartid :", cartid)

    # 04 提交订单
    with allure.step("04 提交订单"):
        data = {
            "goods_id": 10,
            "buy_type": "cart",
            "stock": 1,
            "spec": "",
            "ids": cartid,
            "address_id": 921,
            "payment_id": 4,
            "user_note": "",
            "site_model": 0
        }
        params = {
            "application": "app",
            "application_client_type": "weixin",
            "token": token
        }
        res = kw.post(url="http://shop-xo.hctestedu.com/index.php?s=api/buy/add", params=params, json=data)
        print(res.text)
    # 获取订单id
    with allure.step("04 获取订单id"):
        orderid_list = kw.get_text(res.json(), '$..order_ids')
        orderid = orderid_list[0][0]
        print("orderid :", orderid)

    # 05 订单支付
    with allure.step("05 订单支付"):
        data = {
            "ids": orderid,
            # 1 支付宝,2 微信,4 货到付款
            "payment_id": 4
        }
        params = {
            "application": "app",
            "application_client_type": "weixin",
            "token": token
        }
        res = kw.post(url="http://shop-xo.hctestedu.com/index.php?s=api/order/pay", params=params, json=data)
        print(res.text)
        order_submit_msg = kw.get_text(res.json(), '$..msg')[0]
        assert order_submit_msg =='处理成功'

if __name__ == '__main__':
    test09_submit_order()
