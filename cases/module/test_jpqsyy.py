# conding=utf-8
# @Time : 2021/5/12 14:14
# @Author : SYF
# @File : test_jpqsyy.py
# @Software: PyCharm

import pytest
from pages.JingPinQianShiYinYuan import Jingpinqianshiyinyuan
import time
import re

class TestJingPinQianShiYinYuan():

    def test_01(self, jpqsyy:Jingpinqianshiyinyuan):
        '''不输入女方姓名是否正常'''
        jpqsyy.open("/jingpinqianshiyinyuan/index?channel=online_paytest")
        jpqsyy.empty_girl_name()
        acturl_tips = jpqsyy.get_tips()
        expect_tips = "女方姓名不能为空！"
        assert acturl_tips == expect_tips

    def test_02(self,jpqsyy:Jingpinqianshiyinyuan):
        '''输入女方姓名字数过短是否正常'''
        jpqsyy.open("/jingpinqianshiyinyuan/index?channel=online_paytest")
        jpqsyy.girl_short_name()
        acturl_tips = jpqsyy.get_tips()
        expect_tips = "女方姓名长度不能小于2！"
        assert acturl_tips == expect_tips

    def test_03(self,jpqsyy:Jingpinqianshiyinyuan):
        '''输入女方姓名字数过长是否正常'''
        jpqsyy.open("/jingpinqianshiyinyuan/index?channel=online_paytest")
        jpqsyy.girl_long_name()
        acturl_tips = jpqsyy.get_tips()
        expect_tips = "女方姓名长度不能超过4！"
        assert  acturl_tips == expect_tips

    def test_04(self,jpqsyy:Jingpinqianshiyinyuan):
        '''输入女方姓名为英文是否正常'''
        jpqsyy.open("/jingpinqianshiyinyuan/index?channel=online_paytest")
        jpqsyy.girl_name_is_English()
        acturl_tips = jpqsyy.get_tips()
        expect_tips = "女方姓名必须为汉字！"
        assert acturl_tips == expect_tips

    def test_05(self,jpqsyy:Jingpinqianshiyinyuan):
        '''输入女方姓名为数字是否正常'''
        jpqsyy.open("/jingpinqianshiyinyuan/index?channel=online_paytest")
        jpqsyy.girl_name_is_number()
        acturl_tips = jpqsyy.get_tips()
        expect_tips = "女方姓名必须为汉字！"
        assert acturl_tips == expect_tips

    def test_06(self,jpqsyy:Jingpinqianshiyinyuan):
        '''不输入女方生日是否正常'''
        jpqsyy.open("/jingpinqianshiyinyuan/index?channel=online_paytest")
        jpqsyy.empty_girl_brithday()
        acturl_tips = jpqsyy.get_tips()
        expect_tips = "请选择女方出生日期"
        assert acturl_tips == expect_tips

    def test_07(self,jpqsyy:Jingpinqianshiyinyuan):
        '''不输入男方姓名是否正常'''
        jpqsyy.open("/jingpinqianshiyinyuan/index?channel=online_paytest")
        jpqsyy.empty_boy_name()
        acturl_tips = jpqsyy.get_tips()
        expect_tips = "男方姓名不能为空！"
        assert acturl_tips == expect_tips

    def test_08(self,jpqsyy:Jingpinqianshiyinyuan):
        '''输入男方姓名字数过短是否正常'''
        jpqsyy.open("/jingpinqianshiyinyuan/index?channel=online_paytest")
        jpqsyy.boy_short_name()
        acturl_tips = jpqsyy.get_tips()
        expect_tips = "男方姓名长度不能小于2！"
        assert acturl_tips == expect_tips

    def test_09(self,jpqsyy:Jingpinqianshiyinyuan):
        '''输入男方姓名字数过长是否正常'''
        jpqsyy.open("/jingpinqianshiyinyuan/index?channel=online_paytest")
        jpqsyy.boy_long_name()
        acturl_tips = jpqsyy.get_tips()
        expect_tips = "男方姓名长度不能超过4！"
        assert  acturl_tips == expect_tips

    def test_10(self,jpqsyy:Jingpinqianshiyinyuan):
        '''输入男方姓名为英文是否正常'''
        jpqsyy.open("/jingpinqianshiyinyuan/index?channel=online_paytest")
        jpqsyy.boy_name_is_English()
        acturl_tips = jpqsyy.get_tips()
        expect_tips = "男方姓名必须为汉字！"
        assert acturl_tips == expect_tips

    def test_11(self,jpqsyy:Jingpinqianshiyinyuan):
        '''输入男方姓名为数字是否正常'''
        jpqsyy.open("/jingpinqianshiyinyuan/index?channel=online_paytest")
        jpqsyy.boy_name_is_number()
        acturl_tips = jpqsyy.get_tips()
        expect_tips = "男方姓名必须为汉字！"
        assert acturl_tips == expect_tips

    def test_12(self,jpqsyy:Jingpinqianshiyinyuan):
        '''不输入男方生日是否正常'''
        jpqsyy.open("/jingpinqianshiyinyuan/index?channel=online_paytest")
        jpqsyy.empty_boy_brithday()
        acturl_tips = jpqsyy.get_tips()
        expect_tips = "请选择男方出生日期"
        assert acturl_tips == expect_tips

    def test_13(self, jpqsyy:Jingpinqianshiyinyuan):
        '''输入正常的信息，跳转是否正常'''
        jpqsyy.open("/jingpinqianshiyinyuan/index?channel=online_paytest")
        jpqsyy.normal_information()
        current_url = jpqsyy.get_url()
        acturl_url = re.findall("https://(.+?)/pay?", current_url)[0]
        expect_url = "cs.lingbz.com/jingpinqianshiyinyuan"
        assert  acturl_url == expect_url

    def test_14(self,jpqsyy:Jingpinqianshiyinyuan):
        '''调起微信支付是否正常'''
        jpqsyy.open("/jingpinqianshiyinyuan/index?channel=online_paytest")
        jpqsyy.wechat_pay()
        acturl_title = jpqsyy.get_title()
        expect_title = "灵机支付 - 微信扫码支付"
        assert acturl_title == expect_title

    def test_15(self,jpqsyy:Jingpinqianshiyinyuan):
        '''调起支付宝支付是否正常'''
        jpqsyy.open("/jingpinqianshiyinyuan/index?channel=online_paytest")
        jpqsyy.zfb_pay()
        acturl_title = jpqsyy.get_title()
        expect_title = "支付宝"
        assert acturl_title == expect_title

    def test_16(self,jpqsyy:Jingpinqianshiyinyuan):
        '''跳转到历史订单是否正常'''
        jpqsyy.open("/jingpinqianshiyinyuan/index?channel=online_paytest")
        jpqsyy.click_lsdd()
        current_url = jpqsyy.get_url()
        acturl_tips = re.findall("https://(.+?)/index?", current_url)[0]
        expect_tips = "cs.lingbz.com/orderquery"
        assert acturl_tips == expect_tips

    def test_17(self,jpqsyy:Jingpinqianshiyinyuan):
        '''在历史订单中调起微信支付是否正常'''
        jpqsyy.open("/jingpinqianshiyinyuan/index?channel=online_paytest")
        jpqsyy.dd_wechat_pay()
        acturl_tips = jpqsyy.get_title()
        expect_title = "灵机支付 - 微信扫码支付"
        assert acturl_tips == expect_title

    def test_18(self,jpqsyy:Jingpinqianshiyinyuan):
        '''在历史订单中调起支付宝支付是否正常'''
        jpqsyy.open("/jingpinqianshiyinyuan/index?channel=online_paytest")
        jpqsyy.dd_zfb_pay()
        acturl_title = jpqsyy.get_title()
        expect_title = "支付宝"
        assert acturl_title == expect_title