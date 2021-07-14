from pages.SongShaoGuangYunCheng import Songshaoguangyuncheng
import time
import re

class TestSongShaoGuangYunCheng():

    def test_01(self, ssgyc:Songshaoguangyuncheng):
        '''不填写姓名是否会正常'''
        ssgyc.open("/dashiyunchengheji/index?channel=online_paytest")
        ssgyc.empty_name()
        acturl_tips = ssgyc.get_tips()
        expect_tips = "请填写姓名"
        assert acturl_tips == expect_tips

    def test_02(self, ssgyc:Songshaoguangyuncheng):
        '''中文名称太长提示是否正常'''
        ssgyc.open("/dashiyunchengheji/index?channel=online_paytest")
        ssgyc.long_name()
        acturl_tips = ssgyc.get_tips()
        expect_tips = "姓名不超过6个字"
        assert acturl_tips == expect_tips

    def test_03(self, ssgyc:Songshaoguangyuncheng):
        '''中文名称太短提示是否正常'''
        ssgyc.open("/dashiyunchengheji/index?channel=online_paytest")
        ssgyc.short_name()
        acturl_tips = ssgyc.get_tips()
        expect_tips = "姓名最少2个字"
        assert acturl_tips == expect_tips

    def test_04(self, ssgyc:Songshaoguangyuncheng):
        '''英文名称提示是否正常'''
        ssgyc.open("/dashiyunchengheji/index?channel=online_paytest")
        ssgyc.english_name()
        acturl_tips = ssgyc.get_tips()
        expect_tips = "请输入中文"
        assert acturl_tips == expect_tips


    def test_05(self, ssgyc:Songshaoguangyuncheng):
        '''输入正常的信息跳转到支付页是否正常'''
        ssgyc.open("/dashiyunchengheji/index?channel=online_paytest")
        ssgyc.normal_information()
        current_url = ssgyc.get_url()
        acturl_url = re.findall("https://(.+?)/pay?", current_url)[0]
        expect_url = "cs.lingbz.com/dashiyunchengheji"
        assert acturl_url == expect_url


    def test_06(self, ssgyc:Songshaoguangyuncheng):
        '''调起微信支付是否正常'''
        ssgyc.open("/dashiyunchengheji/index?channel=online_paytest")
        ssgyc.wechat_pay()
        acturl_title = ssgyc.get_title()
        expect_title = "灵机支付 - 微信扫码支付"
        assert acturl_title == expect_title


    def test_07(self, ssgyc:Songshaoguangyuncheng):
        '''调起支付宝支付是否正常'''
        ssgyc.open("/dashiyunchengheji/index?channel=online_paytest")
        ssgyc.zfb_pay()
        acturl_title = ssgyc.get_title()
        expect_title1 = "支付宝"
        expect_title2 = "支付宝 - 网上支付 安全快速！"
        if acturl_title == "支付宝":
            assert acturl_title == expect_title1
        else:
            assert acturl_title == expect_title2
    def test_08(self, ssgyc:Songshaoguangyuncheng):
        '''跳转到历史订单页是否正常'''
        ssgyc.open("/dashiyunchengheji/index?channel=online_paytest")
        ssgyc.lsdd()
        current_url = ssgyc.get_url()
        acturl_url = re.findall("https://(.+?)/index?", current_url)[0]
        expect_url = "cs.lingbz.com/orderquery"
        assert acturl_url == expect_url

    def test_09(self, ssgyc:Songshaoguangyuncheng):
        '''调起历史订单的微信支付是否正常'''
        ssgyc.open("/dashiyunchengheji/index?channel=online_paytest")
        ssgyc.dd_wechat_pay()
        acturl_title = ssgyc.get_title()
        expect_title = "灵机支付 - 微信扫码支付"
        assert acturl_title == expect_title

    def test_10(self, ssgyc:Songshaoguangyuncheng):
        '''调起历史订单的支付宝支付是否正常'''
        ssgyc.open("/dashiyunchengheji/index?channel=online_paytest")
        ssgyc.dd_zfb_pay()
        acturl_title = ssgyc.get_title()
        expect_title1 = "支付宝"
        expect_title2 = "支付宝 - 网上支付 安全快速！"
        if acturl_title == "支付宝":
            assert acturl_title == expect_title1
        else:
            assert acturl_title == expect_title2
