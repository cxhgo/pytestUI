from common.base import Base
import time
import re

class Bazihehun(Base):
    '''定义所需要的元素'''
    ele_girl_name = ("xpath", '//*[@id="root"]/div[2]/div[2]/div/div[1]/div[1]/div[2]/div/div/div[1]/div/input')  # 女方姓名输入框
    ele_girl_birthday = ("xpath", '//*[@id="root"]/div[2]/div[2]/div/div[1]/div[1]/div[2]/div/div/div[2]/div/input')  # 女方出生日期输入框
    ele_boy_name = ("xpath",'//*[@id="root"]/div[2]/div[2]/div/div[1]/div[2]/div[2]/div/div/div[1]/div/input')  # 男方姓名输入框
    ele_boy_birthday = ("xpath",'//*[@id="root"]/div[2]/div[2]/div/div[1]/div[2]/div[2]/div/div/div[2]/div/input')  # 男方出生日期输入框
    ele_ljcs = ("xpath",'//*[@id="root"]/div[2]/div[2]/div/div[1]/div[3]/div/img')  # 立即测算按钮
    ele_tips = ("xpath",'/html/body/div[5]/div/span/div/div/div/div')  # 提示框
    ele_girl_wc = ("xpath",'/html/body/div[2]/div[2]/div/div[1]/div[1]/div[3]')  # 女方完成按钮
    ele_girl_qrzq = ("xpath",'/html/body/div[2]/div[2]/div/div[2]/div[2]/div/button[2]')  # 女方确认正确按钮
    ele_boy_wc = ("xpath",'/html/body/div[3]/div[2]/div/div[1]/div[1]/div[3]')  # 男方完成按钮
    ele_boy_qrzq = ("xpath", '/html/body/div[3]/div[2]/div/div[2]/div[2]/div/button[2]')  # 男方确认正确按钮
    ele_wxzf = ("xpath",'//*[@id="pay"]/div[2]/div[1]/div/div/div[3]/div[1]')  # 微信支付
    ele_zfbzf = ("xpath",'//*[@id="pay"]/div[2]/div[1]/div/div/div[3]/div[2]')  # 支付宝支付
    ele_ylzf = ("xpath",'//*[@id="pay"]/div[2]/div[2]/div[2]/div[2]/ul/li[3]/div[2]/div')  # 银联支付
    ele_ppzf = ("xpath",'//*[@id="pay"]/div[2]/div[2]/div[2]/div[2]/ul/li[4]/div[2]/div')  # paypal支付
    ele_ljzf=("xpath",'//*[@id="pay"]/div[2]/div[1]/div/div/div[3]/div[3]') # 立即支付
    ele_gdzf = ("xpath",'//*[@id="pay"]/div/div[2]/div[2]/div[2]/div')  # 更多支付按钮
    ele_lsdd = ("xpath",'//*[@id="root"]/div[1]/div[3]')  # 历史订单
    ele_ddhsrk = ("xpath",'//*[@id="query"]/div[1]/section/div/div/input')  # 订单号输入框
    ele_ddh = ("xpath",'//*[@id="orderList"]/li[1]/div[3]/div[2]')  # 订单号
    ele_ddtz = ("xpath",'//*[@id="query"]/div[1]/section/button')  # 订单跳转按钮
    ele_gb = ("xpath",'//*[@id="pay"]/div[1]/div/div[1]/img')  # 支付页挽留弹窗的关闭按钮
    ele_paytips1 = ("xpath",'/html/body/div[4]/div[2]/p[2]')  #调起支付后的弹窗
    ele_paytips2 = ("xpath",'/html/body/div[3]/div[2]/p[2]')  #调起支付后的弹窗

    def input_girl_name(self, text):
        '''输入女方名字'''
        self.send(self.ele_girl_name, text)

    def input_boy_name(self, text):
        '''输入男方名字'''
        self.send(self.ele_boy_name, text)

    def choose_girl_birthday(self):
        '''选择女方出生日期'''
        self.click(self.ele_girl_birthday)
        time.sleep(1)
        self.click(self.ele_girl_wc)
        time.sleep(1)
        self.click(self.ele_girl_qrzq)
        time.sleep(1)

    def choose_boy_birthday(self):
        '''选择男方出生日期'''
        self.click(self.ele_boy_birthday)
        time.sleep(1)
        self.click(self.ele_boy_wc)
        time.sleep(1)
        self.click(self.ele_boy_qrzq)
        time.sleep(1)

    def click_ljcs(self):
        '''点击立即测算'''
        self.click(self.ele_ljcs)

    def get_tips(self):
        '''获取toast提示'''
        tips = self.get_text(self.ele_tips)
        return tips

    def get_url(self):
        '''获取当前页面的url'''
        current_url = self.driver.current_url
        return current_url

    def click_wechat_pay(self):
        '''点击微信支付'''
        self.click(self.ele_wxzf)
        self.click(self.ele_ljzf)

    def click_zfb_pay(self):
        '''点击支付宝支付'''
        self.click(self.ele_zfbzf)
        self.click(self.ele_ljzf)

    def click_yl_pay(self):
        '''点击银联支付'''
        self.click(self.ele_ylzf)

    def click_pp_pay(self):
        '''点击paypal支付'''
        self.click(self.ele_ppzf)

    def get_title(self):
        '''获取title'''
        title = self.driver.title
        return title

    def click_gdzf(self):
        '''点击更多支付方式'''
        self.click(self.ele_gdzf)

    def click_lsdd(self):
        '''点击订单入口'''
        time.sleep(2)
        self.click(self.ele_lsdd)
        time.sleep(5)

    def empty_girl_name(self):
        '''不填女方姓名'''
        self.click_ljcs()
        time.sleep(0.5)

    def empty_boy_name(self):
        '''不填男方姓名'''
        self.input_girl_name("若云")
        self.choose_girl_birthday()
        self.click_ljcs()
        time.sleep(0.5)

    def girl_short_name(self):
        '''输入女方名字过短'''
        self.input_girl_name('云')
        self.click_ljcs()
        time.sleep(0.5)

    def girl_long_name(self):
        '''输入女方名字过长'''
        self.input_girl_name('若云若云若云')
        self.click_ljcs()
        time.sleep(0.5)

    def boy_short_name(self):
        '''输入男方名字过短'''
        self.input_girl_name('若云')
        self.choose_girl_birthday()
        self.input_boy_name('若')
        self.click_ljcs()
        time.sleep(0.5)

    def boy_long_name(self):
        '''输入男方名字过长'''
        self.input_girl_name('若云')
        self.choose_girl_birthday()
        self.input_boy_name('若云若云若云')
        self.click_ljcs()
        time.sleep(0.5)

    def girl_english_name(self):
        '''输入英文的女方姓名'''
        self.input_girl_name('ruoyun')
        self.click_ljcs()
        time.sleep(0.5)

    def boy_english_name(self):
        '''输入英文的男方姓名'''
        self.input_girl_name('若云')
        self.choose_girl_birthday()
        self.input_boy_name('ruoyun')
        self.click_ljcs()
        time.sleep(0.5)

    def girl_empty_birthday(self):
        '''不输入女方出生日期'''
        self.input_girl_name('若云')
        self.click_ljcs()
        time.sleep(0.5)

    def boy_empty_birthday(self):
        '''不输入男方出生日期'''
        self.input_girl_name('若云')
        self.choose_girl_birthday()
        self.input_boy_name('若云')
        self.click_ljcs()
        time.sleep(0.5)

    def normal_information(self):
        '''输入正常的信息'''
        self.input_girl_name('若云')
        self.choose_girl_birthday()
        self.input_boy_name('若云')
        self.choose_boy_birthday()
        self.click_ljcs()
        time.sleep(2)

    def wechat_pay(self):
        '''微信支付'''
        self.input_girl_name('若云')
        self.choose_girl_birthday()
        self.input_boy_name('若云')
        self.choose_boy_birthday()
        self.click_ljcs()
        time.sleep(2)
        self.click_wechat_pay()
        time.sleep(2)

    def zfb_pay(self):
        '''支付宝支付'''
        self.input_girl_name('若云')
        self.choose_girl_birthday()
        self.input_boy_name('若云')
        self.choose_boy_birthday()
        self.click_ljcs()
        time.sleep(2)
        self.click_zfb_pay()
        time.sleep(2)

    def yl_pay(self):
        '''银联支付'''
        self.input_girl_name('若云')
        self.choose_girl_birthday()
        self.input_boy_name('若云')
        self.choose_boy_birthday()
        self.click_ljcs()
        time.sleep(2)
        self.click_gdzf()
        self.click_yl_pay()
        time.sleep(4)

    def pp_pay(self):
        '''paypal支付'''
        self.input_girl_name('若云')
        self.choose_girl_birthday()
        self.input_boy_name('若云')
        self.choose_boy_birthday()
        self.click_ljcs()
        time.sleep(2)
        self.click_gdzf()
        self.click_pp_pay()
        time.sleep(4)

    def dd_wechat_pay(self):
        '''在历史订单中调起微信支付'''
        self.input_girl_name('若云')
        self.choose_girl_birthday()
        self.input_boy_name('若云')
        self.choose_boy_birthday()
        self.click_ljcs()
        time.sleep(2)
        self.driver.back()
        time.sleep(1)
        self.driver.back()
        time.sleep(1)
        self.driver.back()
        time.sleep(5)
        self.click_lsdd()
        self.send(self.ele_ddhsrk, self.get_text(self.ele_ddh))
        self.click(self.ele_ddtz)
        time.sleep(2)
        self.click_wechat_pay()
        time.sleep(2)

    def dd_zfb_pay(self):
        '''在历史订单中调起支付宝支付'''
        self.input_girl_name('若云')
        self.choose_girl_birthday()
        self.input_boy_name('若云')
        self.choose_boy_birthday()
        self.click_ljcs()
        time.sleep(2)
        self.driver.back()
        time.sleep(1)
        self.driver.back()
        time.sleep(1)
        self.driver.back()
        time.sleep(5)
        self.click_lsdd()
        self.send(self.ele_ddhsrk, self.get_text(self.ele_ddh))
        self.click(self.ele_ddtz)
        time.sleep(2)
        self.click_zfb_pay()
        time.sleep(2)

    def dd_yl_pay(self):
        '''在历史订单中调起银联支付'''
        self.input_girl_name('若云')
        self.choose_girl_birthday()
        self.input_boy_name('若云')
        self.choose_boy_birthday()
        self.click_ljcs()
        time.sleep(2)
        self.driver.back()
        time.sleep(1)
        self.driver.back()
        time.sleep(1)
        self.driver.back()
        self.click_lsdd()
        self.send(self.ele_ddhsrk, self.get_text(self.ele_ddh))
        self.click(self.ele_ddtz)
        time.sleep(2)
        self.click_gdzf()
        self.click_yl_pay()
        time.sleep(4)

    def dd_pp_pay(self):
        '''在历史订单中调起paypal支付'''
        self.input_girl_name('若云')
        self.choose_girl_birthday()
        self.input_boy_name('若云')
        self.choose_boy_birthday()
        self.click_ljcs()
        time.sleep(2)
        self.driver.back()
        time.sleep(1)
        self.driver.back()
        time.sleep(1)
        self.driver.back()
        self.click_lsdd()
        self.send(self.ele_ddhsrk, self.get_text(self.ele_ddh))
        self.click(self.ele_ddtz)
        time.sleep(2)
        self.click_gdzf()
        self.click_pp_pay()
        time.sleep(4)