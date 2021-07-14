from pages.GeRenZhanXing import Gerenzhanxing
import time
import re

class TestGeRenZhanXing():

    def test_01(self, grzx:Gerenzhanxing):
        '''名字太短是否正常'''
        grzx.open("/gerenzhanxing/index?channel=online_paytest")
        grzx.short_name()
        acturl_tips = grzx.get_tips()
        expect_tips = "姓名最少2个字"
        assert acturl_tips == expect_tips

    def test_02(self, grzx:Gerenzhanxing):
        '''名字太长是否正常'''
        grzx.open("/gerenzhanxing/index?channel=online_paytest")
        grzx.long_name()
        acturl_tips = grzx.get_tips()
        expect_tips = "姓名不超过5个字"
        assert acturl_tips == expect_tips

    def test_03(self, grzx:Gerenzhanxing):
        '''不选择出生时间是否正常'''
        grzx.open("/gerenzhanxing/index?channel=online_paytest")
        grzx.empty_birthday()
        acturl_tips = grzx.get_tips()
        expect_tips = "请选择出生日期"
        assert acturl_tips == expect_tips

    def test_04(self, grzx:Gerenzhanxing):
        '''不选择出生地点是否正常'''
        grzx.open("/gerenzhanxing/index?channel=online_paytest")
        grzx.empty_space()
        acturl_tips = grzx.get_tips()
        expect_tips = "请选择出生地点"
        assert acturl_tips == expect_tips

    def test_05(self, grzx:Gerenzhanxing):
        '''填写正常信息是否正常'''
        grzx.open("/gerenzhanxing/index?channel=online_paytest")
        grzx.normal_information()
        current_url = grzx.get_url()
        acturl_url = re.findall("https://(.+?)/pay?", current_url)[0]
        expect_url = "cs.lingbz.com/gerenzhanxing"
        assert  acturl_url == expect_url

    def test_06(self, grzx:Gerenzhanxing):
        '''调起微信支付是否正常'''
        grzx.open("/gerenzhanxing/index?channel=online_paytest")
        grzx.wechat_pay()
        acturl_title = grzx.get_title()
        expect_title = "灵机支付 - 微信扫码支付"
        assert acturl_title == expect_title

    def test_07(self, grzx:Gerenzhanxing):
        '''调起支付宝支付是否正常'''
        grzx.open("/gerenzhanxing/index?channel=online_paytest")
        grzx.zfb_pay()
        acturl_title = grzx.get_title()
        expect_title1 = "支付宝"
        expect_title2 = "支付宝 - 网上支付 安全快速！"
        if acturl_title == "支付宝":
            assert acturl_title == expect_title1
        else:
            assert acturl_title == expect_title2   

    # def test_08(self, grzx:Gerenzhanxing):
    #     '''历史订单页面是否正常'''
    #     grzx.open("/gerenzhanxing/index?channel=online_paytest")
    #     grzx.lsdd()
    #     current_url = grzx.get_url()
    #     acturl_url = re.findall("https://(.+?)/index?", current_url)[0]
    #     expect_url = "cs.lingbz.com/orderquery"
    #     assert acturl_url == expect_url
    
    # def test_09(self, grzx:Gerenzhanxing):
    #     '''调起历史订单的微信支付是否正常'''
    #     grzx.open("/gerenzhanxing/index?channel=online_paytest")
    #     grzx.dd_wechat_pay()
    #     acturl_title = grzx.get_title()
    #     expect_title = "灵机支付 - 微信扫码支付"
    #     assert acturl_title == expect_title
    
    # def test_10(self, grzx:Gerenzhanxing):
    #     '''调起历史订单的支付宝支付是否正常'''
    #     grzx.open("/gerenzhanxing/index?channel=online_paytest")
    #     grzx.dd_zfb_pay()
    #     acturl_title = grzx.get_title()
    #     expect_title1 = "支付宝"
    #     expect_title2 = "支付宝 - 网上支付 安全快速！"
    #     if acturl_title == "支付宝":
    #         assert acturl_title == expect_title1
    #     else:
    #         assert acturl_title == expect_title2
    