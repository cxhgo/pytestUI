# conding=utf-8
# @Time : 2021/6/11 10:37
# @Author : SYF
# @File : test_nnyc.py
# @Software: PyCharm

from pages.NiuNianYunCheng import Niunianyuncheng
import time
import re


class TestNiuNianYunCheng():

    def test_01(self, nnyc:Niunianyuncheng):
        '''名字太短是否正常'''
        nnyc.open("/mllniunianyuncheng/index?channel=online_paytest")
        nnyc.short_name()
        acturl_tips = nnyc.get_tips()
        expect_tips = "姓名最少2个字"
        assert acturl_tips == expect_tips

    def test_02(self, nnyc:Niunianyuncheng):
        '''名字太长是否会正常'''
        nnyc.open("/mllniunianyuncheng/index?channel=online_paytest")
        nnyc.long_name()
        acturl_tips = nnyc.get_tips()
        expect_tips = "姓名不超过5个字"
        assert acturl_tips == expect_tips

    def test_03(self, nnyc:Niunianyuncheng):
        '''英文姓名太短是否正常'''
        nnyc.open("/mllniunianyuncheng/index?channel=online_paytest")
        nnyc.short_english_name()
        acturl_tips = nnyc.get_tips()
        expect_tips = "英文姓名最少3个字母"
        assert acturl_tips == expect_tips

    def test_04(self, nnyc:Niunianyuncheng):
        '''英文姓名太长是否正常'''
        nnyc.open("/mllniunianyuncheng/index?channel=online_paytest")
        nnyc.long_english_name()
        acturl_tips = nnyc.get_tips()
        expect_tips = "英文姓名不超过10个字母"
        assert acturl_tips == expect_tips

    def test_05(self, nnyc:Niunianyuncheng):
        '''正常填写信息跳转是否正常'''
        nnyc.open("/mllniunianyuncheng/index?channel=online_paytest")
        nnyc.normal_information()
        time.sleep(2)
        current_url = nnyc.get_url()
        acturl_url = re.findall("https://(.+?)/pay?", current_url)[0]
        expect_url = "cs.lingbz.com/mllniunianyuncheng"
        assert acturl_url == expect_url

    def test_06(self, nnyc:Niunianyuncheng):
        '''调起微信支付是否正常'''
        nnyc.open("/mllniunianyuncheng/index?channel=online_paytest")
        nnyc.wechat_pay()
        acturl_title = nnyc.get_title()
        expect_title = "灵机支付 - 微信扫码支付"
        assert acturl_title == expect_title

    def test_07(self, nnyc:Niunianyuncheng):
        '''调起支付宝支付是否正常'''
        nnyc.open("/mllniunianyuncheng/index?channel=online_paytest")
        nnyc.zfb_pay()
        acturl_title = nnyc.get_title()
        expect_title1 = "支付宝"
        expect_title2 = "支付宝 - 网上支付 安全快速！"
        if acturl_title == "支付宝":
            assert acturl_title == expect_title1
        else:
            assert acturl_title == expect_title2

    def test_08(self, nnyc:Niunianyuncheng):
        '''调起历史订单的微信支付是否正常'''
        nnyc.open("/mllniunianyuncheng/index?channel=online_paytest")
        nnyc.dd_wechat_pay()
        acturl_title = nnyc.get_title()
        expect_title = "灵机支付 - 微信扫码支付"
        assert acturl_title == expect_title

    def test_09(self, nnyc:Niunianyuncheng):
        '''调起历史订单的支付宝支付是否正常'''
        nnyc.open("/mllniunianyuncheng/index?channel=online_paytest")
        nnyc.dd_zfb_pay()
        acturl_title = nnyc.get_title()
        expect_title1 = "支付宝"
        expect_title2 = "支付宝 - 网上支付 安全快速！"
        if acturl_title == "支付宝":
            assert acturl_title == expect_title1
        else:
            assert acturl_title == expect_title2