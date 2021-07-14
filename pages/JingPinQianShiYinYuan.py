# conding=utf-8
# @Time : 2021/5/12 14:19
# @Author : SYF
# @File : JingPinQianShiYinYuan.py
# @Software: PyCharm

from common.base import Base
import time
import re

class Jingpinqianshiyinyuan(Base):
    '''定义所需要的元素'''
    ele_girl_name = ("xpath", '//*[@id="root"]/div[2]/div[2]/div[1]/div/div[1]/div/div[1]/div[2]/div/div/div[1]/div/input')  # 女方姓名输入框
    ele_girl_birthday = ("xpath", '//*[@id="root"]/div[2]/div[2]/div[1]/div/div[1]/div/div[1]/div[2]/div/div/div[2]/div/input')  # 女方出生日期输入框
    ele_boy_name = ("xpath", '//*[@id="root"]/div[2]/div[2]/div[1]/div/div[1]/div/div[2]/div[2]/div/div/div[1]/div/input')  # 男方姓名输入框
    ele_boy_birthday = ("xpath", '//*[@id="root"]/div[2]/div[2]/div[1]/div/div[1]/div/div[2]/div[2]/div/div/div[2]/div/input')  # 男方出生日期输入框
    ele_ckqsyy = ("xpath", '//*[@id="root"]/div[2]/div[2]/div[1]/div/div[2]/div/img')  # 查看前世姻缘按钮
    ele_tips = ("xpath", '/html/body/div[6]/div/span/div/div/div/div')  # 提示框
    ele_girl_wc = ("xpath", '/html/body/div[3]/div[3]/div[1]/div[2]')  # 女方完成按钮
    ele_girl_qrzq = ("xpath", '/html/body/div[3]/div[2]/div[3]/div[2]/span')  # 女方确认正确按钮
    ele_boy_wc = ("xpath", '/html/body/div[4]/div[3]/div[1]/div[2]')  # 男方完成按钮
    ele_boy_qrzq = ("xpath", '/html/body/div[4]/div[2]/div[3]/div[2]/span')  # 男方确认正确按钮
    ele_lqbg=("xpath",'//*[@id="root"]/div[1]/div[2]/div[2]/img')  # 领取报告按钮
    ele_wxzf = ("xpath", '//*[@id="root"]/div[1]/div[3]/div/div/div[1]/div[3]/div/label')  # 微信支付
    ele_zfbzf = ("xpath", '//*[@id="root"]/div[1]/div[3]/div/div/div[1]/div[4]/div/label')  # 支付宝支付
    ele_ljjsnr=("xpath",'//*[@id="root"]/div[1]/div[3]/div/div/div[2]')  #立即解锁内容按钮
    ele_lsdd = ("xpath", '//*[@id="root"]/div[2]/div[2]/p/a')  # 历史订单
    ele_ddhsrk = ("xpath", '//*[@id="query"]/div[1]/section/div/div/input')  # 订单号输入框
    ele_ddh = ("xpath", '//*[@id="orderList"]/li/div[3]/div[2]')  # 订单号
    ele_djck = ("xpath", '//*[@id="orderList"]/li/div[5]')  # 点击查看按钮
    ele_lsdjck=("xpath",'//*[@id="orderList"]/li[1]/div[5]')#历史订单点击查看按钮
    ele_hbmb =("xpath",'//*[@id="root"]/div[1]/div/button')#红包领取按钮
    ele_gb = ("xpath", '//*[@id="pay"]/div[1]/div/div[1]/img')  # 支付页挽留弹窗的关闭按钮
    ele_paytips1 = ("xpath", '/html/body/div[4]/div[2]/p[2]')  # 调起支付后的弹窗

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

    def click_ckqsyy(self):
        '''点击查看前世姻缘'''
        self.click(self.ele_ckqsyy)

    def click_lqbg(self):
        '''点击领取报告按钮'''
        self.click(self.ele_lqbg)

    def click_ljjsnr(self):
        '''点击立即解锁内容按钮'''
        self.click(self.ele_ljjsnr)

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

    def click_zfb_pay(self):
        '''点击支付宝支付'''
        self.click(self.ele_zfbzf)

    def get_title(self):
        '''获取title'''
        title = self.driver.title
        return title

    def click_lsdd(self):
        '''点击订单入口'''
        self.click(self.ele_lsdd)
        time.sleep(5)

    def click_djck(self):
        '''点击查看按钮'''
        self.click(self.ele_djck)

    def empty_girl_name(self):
        '''不填女方姓名'''
        self.click_ckqsyy()
        time.sleep(0.5)

    def empty_girl_brithday(self):
        '''不填女方生日'''
        self.input_girl_name("苏雪")
        self.click_ckqsyy()
        time.sleep(0.5)

    def girl_short_name(self):
        '''输入女方名字过短'''
        self.input_girl_name("苏")
        self.click_ckqsyy()
        time.sleep(0.5)

    def girl_long_name(self):
        '''输入女方名字过长'''
        self.input_girl_name('苏雪入梦来')
        self.click_ckqsyy()
        time.sleep(0.5)

    def girl_name_is_English(self):
        '''输入女方名字为英文'''
        self.input_girl_name("SuXue")
        self.click_ckqsyy()
        time.sleep(0.5)

    def girl_name_is_number(self):
        '''输入女方名字为数字'''
        self.input_girl_name("9527")
        self.click_ckqsyy()
        time.sleep(0.5)

    def empty_boy_name(self):
        '''不填男方名称'''
        self.input_girl_name("苏雪")
        self.choose_girl_birthday()
        self.click_ckqsyy()
        time.sleep(0.5)

    def empty_boy_brithday(self):
        '''不填男方生日'''
        self.input_girl_name("苏雪")
        self.choose_girl_birthday()
        self.input_boy_name("秦天")
        self.click_ckqsyy()
        time.sleep(0.5)

    def boy_short_name(self):
        '''输入男方名字过短'''
        self.input_girl_name("苏雪")
        self.choose_girl_birthday()
        self.input_boy_name("秦")
        self.click_ckqsyy()
        time.sleep(0.5)

    def boy_long_name(self):
        '''输入男方名字过长'''
        self.input_girl_name("苏雪")
        self.choose_girl_birthday()
        self.input_boy_name("秦天水一色")
        self.click_ckqsyy()
        time.sleep(0.5)

    def boy_name_is_English(self):
        '''输入男方名字为英文'''
        self.input_girl_name("苏雪")
        self.choose_girl_birthday()
        self.input_boy_name("QinTian")
        self.click_ckqsyy()
        time.sleep(0.5)

    def boy_name_is_number(self):
        '''输入男方名字为数字'''
        self.input_girl_name("苏雪")
        self.choose_girl_birthday()
        self.input_boy_name("9527")
        self.click_ckqsyy()
        time.sleep(0.5)

    def normal_information(self):
        '''输入正常的信息'''
        self.input_girl_name('苏雪')
        self.choose_girl_birthday()
        self.input_boy_name('秦天')
        self.choose_boy_birthday()
        self.click_ckqsyy()
        time.sleep(2)

    def wechat_pay(self):
        '''微信支付'''
        self.input_girl_name('苏雪')
        self.choose_girl_birthday()
        self.input_boy_name('秦天')
        self.choose_boy_birthday()
        self.click_ckqsyy()
        time.sleep(15)
        self.click_lqbg()
        self.click_wechat_pay()
        self.click_ljjsnr()
        time.sleep(2)

    def zfb_pay(self):
        '''支付宝支付'''
        self.input_girl_name('苏雪')
        self.choose_girl_birthday()
        self.input_boy_name('秦天')
        self.choose_boy_birthday()
        self.click_ckqsyy()
        time.sleep(15)
        self.click_lqbg()
        self.click_zfb_pay()
        self.click_ljjsnr()
        time.sleep(2)

    def dd_wechat_pay(self):
        '''在历史订单中调起微信支付'''
        self.input_girl_name('苏雪')
        self.choose_girl_birthday()
        self.input_boy_name('秦天')
        self.choose_boy_birthday()
        self.click_ckqsyy()
        time.sleep(2)
        self.driver.back()
        time.sleep(1)
        self.driver.back()
        self.click_lsdd()
        # self.send(self.ele_ddhsrk, self.get_text(self.ele_ddh))
        # self.click(self.ele_djck)
        self.click(self.ele_lsdjck)
        # self.click(self.ele_hbmb)
        # time.sleep(3)
        # self.driver.back()
        time.sleep(15)
        self.click_lqbg()
        self.click_wechat_pay()
        self.click_ljjsnr()
        time.sleep(2)

    def dd_zfb_pay(self):
        '''在历史订单中调起支付宝支付'''
        self.input_girl_name('苏雪')
        self.choose_girl_birthday()
        self.input_boy_name('秦天')
        self.choose_boy_birthday()
        self.click_ckqsyy()
        time.sleep(2)
        self.driver.back()
        time.sleep(1)
        self.driver.back()
        self.click_lsdd()
        # self.send(self.ele_ddhsrk, self.get_text(self.ele_ddh))
        # self.click(self.ele_djck)
        self.click(self.ele_lsdjck)
        # self.click(self.ele_hbmb)
        # time.sleep(3)
        # self.driver.back()
        time.sleep(15)
        self.click_lqbg()
        self.click_zfb_pay()
        self.click_ljjsnr()
        time.sleep(2)