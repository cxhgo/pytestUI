from pages.ZhanWeiZhongJingPi import Zhanweizhongjingpi
import time
import re

class TestZhanWeiZhongJingPi():
    
    def test_01(self, zwzjp:Zhanweizhongjingpi):
        '''名字太短是否正常'''
        zwzjp.open("/zwzjingpi/index?channel=online_paytest")
        zwzjp.short_name()
        acturl_tips = zwzjp.get_tips()
        expect_tips = "姓名最少2个字"
        assert acturl_tips == expect_tips

    def test_02(self, zwzjp:Zhanweizhongjingpi):
        '''名字太长是否会正常'''
        zwzjp.open("/zwzjingpi/index?channel=online_paytest")
        zwzjp.long_name()
        acturl_tips = zwzjp.get_tips()
        expect_tips = "姓名不超过5个字"
        assert acturl_tips == expect_tips

    def test_03(self, zwzjp:Zhanweizhongjingpi):
        '''英文姓名太短是否正常'''
        zwzjp.open("/zwzjingpi/index?channel=online_paytest")
        zwzjp.short_english_name()
        acturl_tips = zwzjp.get_tips()
        expect_tips = "英文姓名最少3个字母"
        assert acturl_tips == expect_tips

    def test_04(self, zwzjp:Zhanweizhongjingpi):
        '''英文姓名太长是否正常'''
        zwzjp.open("/zwzjingpi/index?channel=online_paytest")
        zwzjp.long_english_name()
        acturl_tips = zwzjp.get_tips()
        expect_tips = "英文姓名不超过10个字母"
        assert acturl_tips == expect_tips

    def test_05(self, zwzjp:Zhanweizhongjingpi):
        '''正常填写信息跳转是否正常'''
        zwzjp.open("/zwzjingpi/index?channel=online_paytest")
        zwzjp.normal_information()
        time.sleep(2)
        current_url = zwzjp.get_url()
        acturl_url = re.findall("https://(.+?)order_id", current_url)[0]
        expect_url = "cs.lingbz.com/pay/zwzjingpi?"
        assert acturl_url == expect_url

    def test_06(self, zwzjp:Zhanweizhongjingpi):
        '''调起微信支付是否正常'''
        zwzjp.open("/zwzjingpi/index?channel=online_paytest")
        zwzjp.wechat_pay()
        acturl_title = zwzjp.get_title()
        expect_title = "灵机支付 - 微信扫码支付"
        assert acturl_title == expect_title

    def test_07(self, zwzjp:Zhanweizhongjingpi):
        '''调起支付宝支付是否正常'''
        zwzjp.open("/zwzjingpi/index?channel=online_paytest")
        zwzjp.zfb_pay()
        acturl_title = zwzjp.get_title()
        expect_title1 = "支付宝"
        expect_title2 = "支付宝 - 网上支付 安全快速！"
        if acturl_title == "支付宝":
            assert acturl_title == expect_title1
        else:
            assert acturl_title == expect_title2

    def test_08(self, zwzjp:Zhanweizhongjingpi):
        '''调起银联支付是否正常'''
        zwzjp.open("/zwzjingpi/index?channel=online_paytest")
        zwzjp.yl_pay()
        acturl_title = zwzjp.get_title()
        if acturl_title == 'Unionpay Online Payment-Comprehensive online trading transfer and liquidation platform!':
            assert True
        else:
            expect_title = "银联在线支付-银行卡综合性网上交易转接清算平台！"
            assert acturl_title == expect_title

    def test_09(self, zwzjp:Zhanweizhongjingpi):
        '''调起paypal支付是否正常'''
        zwzjp.open("/zwzjingpi/index?channel=online_paytest")
        zwzjp.pp_pay()
        acturl_title = zwzjp.get_title()
        expect_title = "登录您的PayPal账户"
        assert acturl_title == expect_title

    def test_10(self, zwzjp:Zhanweizhongjingpi):
        '''进入历史订单是否正常'''
        zwzjp.open("/zwzjingpi/index?channel=online_paytest")
        zwzjp.lsdd()
        current_url = zwzjp.get_url()
        acturl_url = re.findall("https://(.+?)/index?", current_url)[0]
        expect_url = "cs.lingbz.com/orderquery"
        assert acturl_url == expect_url

    def test_11(self, zwzjp:Zhanweizhongjingpi):
        '''调起历史订单的微信支付是否正常'''
        zwzjp.open("/zwzjingpi/index?channel=online_paytest")
        zwzjp.dd_wechat_pay()
        acturl_title = zwzjp.get_title()
        expect_title = "灵机支付 - 微信扫码支付"
        assert acturl_title == expect_title

    def test_12(self, zwzjp:Zhanweizhongjingpi):
        '''调起历史订单的支付宝支付是否正常'''
        zwzjp.open("/zwzjingpi/index?channel=online_paytest")
        zwzjp.dd_zfb_pay()
        acturl_title = zwzjp.get_title()
        expect_title1 = "支付宝"
        expect_title2 = "支付宝 - 网上支付 安全快速！"
        if acturl_title == "支付宝":
            assert acturl_title == expect_title1
        else:
            assert acturl_title == expect_title2

    def test_13(self, zwzjp:Zhanweizhongjingpi):
        '''调起历史订单的银联支付是否正常'''
        zwzjp.open("/zwzjingpi/index?channel=online_paytest")
        zwzjp.dd_yl_pay()
        acturl_title = zwzjp.get_title()
        if acturl_title == 'Unionpay Online Payment-Comprehensive online trading transfer and liquidation platform!':
            assert True
        else:
            expect_title = "银联在线支付-银行卡综合性网上交易转接清算平台！"
            assert acturl_title == expect_title

    def test_14(self, zwzjp:Zhanweizhongjingpi):
        '''调起历史订单的paypal支付是否正常'''
        zwzjp.open("/zwzjingpi/index?channel=online_paytest")
        zwzjp.dd_pp_pay()
        acturl_title = zwzjp.get_title()
        expect_title = "登录您的PayPal账户"
        assert acturl_title == expect_title
