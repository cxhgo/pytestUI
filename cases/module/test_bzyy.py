import pytest
from pages.BaZiYinYuan import Baziyinyuan
import time
import re


class TestBaZiYinYuan():

    def test_01(self, bzyy:Baziyinyuan):
        '''名字太短是否正常'''
        bzyy.open("/baziyinyuan/index?channel=online_paytest")
        bzyy.short_name()
        acturl_tips = bzyy.get_tips()
        expect_tips = "姓名最少2个字"
        assert acturl_tips == expect_tips

    def test_02(self, bzyy:Baziyinyuan):
        '''名字太长是否会正常'''
        bzyy.open("/baziyinyuan/index?channel=online_paytest")
        bzyy.long_name()
        acturl_tips = bzyy.get_tips()
        expect_tips = "姓名不超过5个字"
        assert acturl_tips == expect_tips

    def test_03(self, bzyy:Baziyinyuan):
        '''英文姓名太短是否正常'''
        bzyy.open("/baziyinyuan/index?channel=online_paytest")
        bzyy.short_english_name()
        acturl_tips = bzyy.get_tips()
        expect_tips = "英文姓名最少3个字母"
        assert acturl_tips == expect_tips

    def test_04(self, bzyy:Baziyinyuan):
        '''英文姓名太长是否正常'''
        bzyy.open("/baziyinyuan/index?channel=online_paytest")
        bzyy.long_english_name()
        acturl_tips = bzyy.get_tips()
        expect_tips = "英文姓名不超过10个字母"
        assert acturl_tips == expect_tips

    def test_05(self, bzyy:Baziyinyuan):
        '''正常填写信息跳转是否正常'''
        bzyy.open("/baziyinyuan/index?channel=online_paytest")
        bzyy.normal_information()
        time.sleep(2)
        current_url = bzyy.get_url()
        acturl_url = re.findall("https://(.+?)/newpay?", current_url)[0]
        expect_url = "cs.lingbz.com/baziyinyuan"
        assert acturl_url == expect_url

    def test_06(self, bzyy:Baziyinyuan):
        '''调起微信支付是否正常'''
        bzyy.open("/baziyinyuan/index?channel=online_paytest")
        bzyy.wechat_pay()
        acturl_title = bzyy.get_title()
        expect_title = "灵机支付 - 微信扫码支付"
        assert acturl_title == expect_title

    def test_07(self, bzyy:Baziyinyuan):
        '''调起支付宝支付是否正常'''
        bzyy.open("/baziyinyuan/index?channel=online_paytest")
        bzyy.zfb_pay()
        acturl_title = bzyy.get_title()
        expect_title1 = "支付宝"
        expect_title2 = "支付宝 - 网上支付 安全快速！"
        if acturl_title == "支付宝":
            assert acturl_title == expect_title1
        else:
            assert acturl_title == expect_title2

    def test_08(self, bzyy:Baziyinyuan):
        '''调起银联支付是否正常'''
        bzyy.open("/baziyinyuan/index?channel=online_paytest")
        bzyy.yl_pay()
        acturl_title = bzyy.get_title()
        if acturl_title == 'Unionpay Online Payment-Comprehensive online trading transfer and liquidation platform!':
            assert True
        else:
            expect_title = "银联在线支付-银行卡综合性网上交易转接清算平台！"
            assert acturl_title == expect_title

    def test_09(self, bzyy:Baziyinyuan):
        '''调起paypal支付是否正常'''
        bzyy.open("/baziyinyuan/index?channel=online_paytest")
        bzyy.pp_pay()
        acturl_title = bzyy.get_title()
        expect_title = "登录您的PayPal账户"
        assert acturl_title == expect_title

    def test_10(self, bzyy:Baziyinyuan):
        '''进入历史订单是否正常'''
        bzyy.open("/baziyinyuan/index?channel=online_paytest")
        bzyy.lsdd()
        current_url = bzyy.get_url()
        acturl_url = re.findall("https://(.+?)/index?", current_url)[0]
        expect_url = "cs.lingbz.com/orderquery"
        assert acturl_url == expect_url

    def test_11(self, bzyy:Baziyinyuan):
        '''调起历史订单的微信支付是否正常'''
        bzyy.open("/baziyinyuan/index?channel=online_paytest")
        bzyy.dd_wechat_pay()
        acturl_title = bzyy.get_title()
        expect_title = "灵机支付 - 微信扫码支付"
        assert acturl_title == expect_title

    def test_12(self, bzyy:Baziyinyuan):
        '''调起历史订单的支付宝支付是否正常'''
        bzyy.open("/baziyinyuan/index?channel=online_paytest")
        bzyy.dd_zfb_pay()
        acturl_title = bzyy.get_title()
        expect_title1 = "支付宝"
        expect_title2 = "支付宝 - 网上支付 安全快速！"
        if acturl_title == "支付宝":
            assert acturl_title == expect_title1
        else:
            assert acturl_title == expect_title2

    def test_13(self, bzyy:Baziyinyuan):
        '''调起历史订单的银联支付是否正常'''
        bzyy.open("/baziyinyuan/index?channel=online_paytest")
        bzyy.dd_yl_pay()
        acturl_title = bzyy.get_title()
        if acturl_title == 'Unionpay Online Payment-Comprehensive online trading transfer and liquidation platform!':
            assert True
        else:
            expect_title = "银联在线支付-银行卡综合性网上交易转接清算平台！"
            assert acturl_title == expect_title

    def test_14(self, bzyy:Baziyinyuan):
        '''调起历史订单的paypal支付是否正常'''
        bzyy.open("/baziyinyuan/index?channel=online_paytest")
        bzyy.dd_pp_pay()
        acturl_title = bzyy.get_title()
        expect_title = "登录您的PayPal账户"
        assert acturl_title == expect_title
