from pages.LunHuiShu import Lunhuishu
import time
import re

class TestLunHuiShu():


    def test_01(self, lhs:Lunhuishu):
        '''输入中文姓名太短是否正常'''
        lhs.open("/lunhuishu/index?channel=online_paytest")
        lhs.short_name()
        acturl_tips = lhs.get_tips()
        expect_tips = "姓名最少2个字"
        assert acturl_tips == expect_tips

    def test_02(self, lhs:Lunhuishu):
        '''输入中文姓名太长是否正常'''
        lhs.open("/lunhuishu/index?channel=online_paytest")
        lhs.long_name()
        acturl_tips = lhs.get_tips()
        expect_tips = "姓名不超过5个字"
        assert acturl_tips == expect_tips

    def test_03(self, lhs:Lunhuishu):
        '''输入英文姓名太短是否正常'''
        lhs.open("/lunhuishu/index?channel=online_paytest")
        lhs.short_english_name()
        acturl_tips = lhs.get_tips()
        expect_tips = "英文姓名最少3个字母"
        assert acturl_tips == expect_tips

    def test_04(self, lhs:Lunhuishu):
        '''输入英文姓名太长是否正常'''
        lhs.open("/lunhuishu/index?channel=online_paytest")
        lhs.long_english_name()
        acturl_tips = lhs.get_tips()
        expect_tips = "英文姓名不超过10个字母"
        assert acturl_tips == expect_tips

    def test_05(self, lhs:Lunhuishu):
        '''输入正常的信息是否正常'''
        lhs.open("/lunhuishu/index?channel=online_paytest")
        lhs.normal_information()
        current_url = lhs.get_url()
        acturl_url = re.findall("https://(.+?)/pay?", current_url)[0]
        expect_url = "cs.lingbz.com/lunhuishu"
        assert  acturl_url == expect_url

    def test_06(self, lhs:Lunhuishu):
        '''调起微信支付是否正常'''
        lhs.open("/lunhuishu/index?channel=online_paytest")
        lhs.wechat_pay()
        acturl_title = lhs.get_title()
        expect_title = "灵机支付 - 微信扫码支付"
        assert acturl_title == expect_title

    def test_07(self, lhs:Lunhuishu):
        '''调起支付宝支付是否正常'''
        lhs.open("/lunhuishu/index?channel=online_paytest")
        lhs.zfb_pay()
        acturl_title = lhs.get_title()
        expect_title1 = "支付宝"
        expect_title2 = "支付宝 - 网上支付 安全快速！"
        if acturl_title == "支付宝":
            assert acturl_title == expect_title1
        else:
            assert acturl_title == expect_title2


    def test_08(self, lhs:Lunhuishu):
        '''跳转到历史订单是否正常'''
        lhs.open("/lunhuishu/index?channel=online_paytest")
        lhs.lsdd()
        current_url = lhs.get_url()
        acturl_url = re.findall("https://(.+?)/index?", current_url)[0]
        expect_url = "cs.lingbz.com/orderquery"
        assert acturl_url == expect_url

    def test_09(self,lhs:Lunhuishu):
        '''调起历史订单的微信支付是否正常'''
        lhs.open("/lunhuishu/index?channel=online_paytest")
        lhs.dd_wechat_pay()
        acturl_title = lhs.get_title()
        expect_title = "灵机支付 - 微信扫码支付"
        assert acturl_title == expect_title

    def test_10(self, lhs:Lunhuishu):
        '''调起历史订单的支付宝支付是否正常'''
        lhs.open("/lunhuishu/index?channel=online_paytest")
        lhs.dd_zfb_pay()
        acturl_title = lhs.get_title()
        expect_title1 = "支付宝"
        expect_title2 = "支付宝 - 网上支付 安全快速！"
        if acturl_title == "支付宝":
            assert acturl_title == expect_title1
        else:
            assert acturl_title == expect_title2