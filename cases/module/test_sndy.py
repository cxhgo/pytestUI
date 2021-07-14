from pages.ShiNianDaYun import Shiniandayun
import time
import re

class TestShiNianDaYun():

    def test_01(self, sndy:Shiniandayun):
        '''不输入姓名是否正常'''
        sndy.open("/jingpinshiniandayun/index?channel=online_paytest")
        sndy.empty_name()
        acturl_tips = sndy.get_tips()
        expect_tips = "请填写姓名"
        assert acturl_tips == expect_tips

    def test_02(self, sndy:Shiniandayun):
        '''名字太短是否正常'''
        sndy.open("/jingpinshiniandayun/index?channel=online_paytest")
        sndy.short_name()
        acturl_tips = sndy.get_tips()
        expect_tips = "姓名最少2个字"
        assert acturl_tips == expect_tips

    def test_03(self, sndy:Shiniandayun):
        '''名字太长是否会正常'''
        sndy.open("/jingpinshiniandayun/index?channel=online_paytest")
        sndy.long_name()
        acturl_tips = sndy.get_tips()
        expect_tips = "姓名不超过5个字"
        assert acturl_tips == expect_tips


    def test_04(self, sndy:Shiniandayun):
        '''英文姓名是否正常'''
        sndy.open("/jingpinshiniandayun/index?channel=online_paytest")
        sndy.english_name()
        acturl_tips = sndy.get_tips()
        expect_tips = "请输入中文"
        assert acturl_tips == expect_tips

    def test_05(self, sndy:Shiniandayun):
        '''正常填写信息跳转是否正常'''
        sndy.open("/jingpinshiniandayun/index?channel=online_paytest")
        sndy.normal_information()
        time.sleep(2)
        current_url = sndy.get_url()
        acturl_url = re.findall("https://(.+?)/pay?", current_url)[0]
        expect_url = "cs.lingbz.com/jingpinshiniandayun"
        assert acturl_url == expect_url

    def test_06(self, sndy:Shiniandayun):
        '''调起微信支付是否正常'''
        sndy.open("/jingpinshiniandayun/index?channel=online_paytest")
        sndy.wechat_pay()
        acturl_title = sndy.get_title()
        expect_title = "灵机支付 - 微信扫码支付"
        assert acturl_title == expect_title

    def test_07(self, sndy:Shiniandayun):
        '''调起支付宝支付是否正常'''
        sndy.open("/jingpinshiniandayun/index?channel=online_paytest")
        sndy.zfb_pay()
        acturl_title = sndy.get_title()
        expect_title1 = "支付宝"
        expect_title2 = "支付宝 - 网上支付 安全快速！"
        if acturl_title == "支付宝":
            assert acturl_title == expect_title1
        else:
            assert acturl_title == expect_title2


    def test_08(self, sndy:Shiniandayun):
        '''进入历史订单是否正常'''
        sndy.open("/jingpinshiniandayun/index?channel=online_paytest")
        sndy.lsdd()
        current_url = sndy.get_url()
        acturl_url = re.findall("https://(.+?)/index?", current_url)[0]
        expect_url = "cs.lingbz.com/orderquery"
        assert acturl_url == expect_url

    def test_09(self, sndy:Shiniandayun):
        '''调起历史订单的微信支付是否正常'''
        sndy.open("/jingpinshiniandayun/index?channel=online_paytest")
        sndy.dd_wechat_pay()
        acturl_title = sndy.get_title()
        expect_title = "灵机支付 - 微信扫码支付"
        assert acturl_title == expect_title

    def test_10(self, sndy:Shiniandayun):
        '''调起历史订单的支付宝支付是否正常'''
        sndy.open("/jingpinshiniandayun/index?channel=online_paytest")
        sndy.dd_zfb_pay()
        acturl_title = sndy.get_title()
        expect_title1 = "支付宝"
        expect_title2 = "支付宝 - 网上支付 安全快速！"
        if acturl_title == "支付宝":
            assert acturl_title == expect_title1
        else:
            assert acturl_title == expect_title2

