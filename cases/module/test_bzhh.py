import pytest
from pages.BaZiHeHun import Bazihehun
import time
import re

class TestBzZiHeHun():

    def test_01(self,bzhh:Bazihehun):
        '''不输入女方姓名是否正常'''
        bzhh.open("/bazihehun/index?channel=online_paytest")
        bzhh.empty_girl_name()
        acturl_tips=bzhh.get_tips()
        expect_tips = "女方姓名不能为空！"
        assert acturl_tips == expect_tips

    def test_02(self, bzhh:Bazihehun):
        '''不输入男方姓名是否正常'''
        bzhh.open("/bazihehun/index?channel=online_paytest")
        bzhh.empty_boy_name()
        acturl_tips = bzhh.get_tips()
        expect_tips = "男方姓名不能为空！"
        assert acturl_tips == expect_tips

    def test_03(self, bzhh:Bazihehun):
        '''女方姓名过短是否正常'''
        bzhh.open("/bazihehun/index?channel=online_paytest")
        bzhh.girl_short_name()
        acturl_tips = bzhh.get_tips()
        expect_tips = "女方姓名长度不能小于2！"
        assert acturl_tips == expect_tips


    def test_04(self, bzhh:Bazihehun):
        '''女方姓名过长是否正常'''
        bzhh.open("/bazihehun/index?channel=online_paytest")
        bzhh.girl_long_name()
        acturl_tips = bzhh.get_tips()
        expect_tips = "女方姓名长度不能超过4！"
        assert acturl_tips == expect_tips

    def test_05(self, bzhh:Bazihehun):
        '''输入长度过短的男方中文姓名'''
        bzhh.open("/bazihehun/index?channel=online_paytest")
        bzhh.boy_short_name()
        acturl_tips = bzhh.get_tips()
        expect_tips = "男方姓名长度不能小于2！"
        assert acturl_tips == expect_tips

    def test_06(self, bzhh:Bazihehun):
        '''输入长度过长的男方中文姓名'''
        bzhh.open("/bazihehun/index?channel=online_paytest")
        bzhh.boy_long_name()
        acturl_tips = bzhh.get_tips()
        expect_tips = "男方姓名长度不能超过4！"
        assert acturl_tips == expect_tips

    def test_07(self, bzhh:Bazihehun):
        '''女方姓名输入英文姓名'''
        bzhh.open("/bazihehun/index?channel=online_paytest")
        bzhh.girl_english_name()
        acturl_tips = bzhh.get_tips()
        expect_tips = "女方姓名必须为汉字！"
        assert acturl_tips == expect_tips

    def test_08(self, bzhh:Bazihehun):
        '''男方姓名输入英文姓名'''
        bzhh.open("/bazihehun/index?channel=online_paytest")
        bzhh.boy_english_name()
        acturl_tips = bzhh.get_tips()
        expect_tips = "男方姓名必须为汉字！"
        assert acturl_tips == expect_tips

    def test_09(self, bzhh:Bazihehun):
        '''不输入女方出生日期是否正常'''
        bzhh.open("/bazihehun/index?channel=online_paytest")
        bzhh.girl_empty_birthday()
        acturl_tips = bzhh.get_tips()
        expect_tips = "请选择女方出生日期"
        assert acturl_tips == expect_tips


    def test_10(self, bzhh:Bazihehun):
        '''不输入男方出生日期是否正常'''
        bzhh.open("/bazihehun/index?channel=online_paytest")
        bzhh.boy_empty_birthday()
        acturl_tips = bzhh.get_tips()
        expect_tips = "请选择男方出生日期"
        assert acturl_tips == expect_tips

    def test_11(self, bzhh:Bazihehun):
        '''输入正常的信息，跳转是否正常'''
        bzhh.open("/bazihehun/index?channel=online_paytest")
        bzhh.normal_information()
        current_url = bzhh.get_url()
        acturl_url = re.findall("https://(.+?)/pay?", current_url)[0]
        expect_url = "cs.lingbz.com/bazihehun"
        assert  acturl_url == expect_url

    def test_12(self, bzhh:Bazihehun):
        '''调起微信支付是否正常'''
        bzhh.open("/bazihehun/index?channel=online_paytest")
        bzhh.wechat_pay()
        acturl_tips = bzhh.get_title()
        expect_title = "灵机支付 - 微信扫码支付"
        assert acturl_tips == expect_title

    def test_13(self, bzhh:Bazihehun):
        '''调起支付宝支付是否正常'''
        bzhh.open("/bazihehun/index?channel=online_paytest")
        bzhh.zfb_pay()
        acturl_title = bzhh.get_title()
        expect_title1 = "支付宝"
        expect_title2 = "支付宝 - 网上支付 安全快速！"
        if acturl_title == "支付宝":
            assert acturl_title == expect_title1
        else:
            assert acturl_title == expect_title2

    # def test_16(self, bzhh:Bazihehun):
    #     '''跳转到历史订单是否正常'''
    #     bzhh.open("/bazihehun/index?channel=online_paytest")
    #     bzhh.click_lsdd()
    #     current_url = bzhh.get_url()
    #     acturl_tips = re.findall("https://(.+?)/index?", current_url)[0]
    #     expect_tips = "cs.lingbz.com/orderquery"
    #     assert acturl_tips == expect_tips
    # 
    # def test_17(self, bzhh:Bazihehun):
    #     '''在历史订单中调起微信支付是否正常'''
    #     bzhh.open("/bazihehun/index?channel=online_paytest")
    #     bzhh.dd_wechat_pay()
    #     acturl_tips = bzhh.get_title()
    #     expect_title = "灵机支付 - 微信扫码支付"
    #     assert acturl_tips == expect_title
    # 
    # def test_18(self, bzhh:Bazihehun):
    #     '''在历史订单中调起支付宝支付是否正常'''
    #     bzhh.open("/bazihehun/index?channel=online_paytest")
    #     bzhh.dd_zfb_pay()
    #     acturl_title = bzhh.get_title()
    #     expect_title1 = "支付宝"
    #     expect_title2 = "支付宝 - 网上支付 安全快速！"
    #     if acturl_title == "支付宝":
    #         assert acturl_title == expect_title1
    #     else:
    #         assert acturl_title == expect_title2