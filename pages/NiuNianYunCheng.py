# conding=utf-8
# @Time : 2021/6/11 11:09
# @Author : SYF
# @File : NiuNianYunCheng.py
# @Software: PyCharm

from common.base import Base
import time

class Niunianyuncheng(Base):
    '''定义所需要的元素'''
    ele_ckys= ('xpath', '//*[@id="page-index"]/div/div[2]/div[2]/img[2]')  # 查看运势按钮
    ele_name = ('xpath', '//*[@id="page-index"]/div[1]/div[1]/div/div/div[1]/input')  # 姓名输入框
    ele_birthday = ('xpath', '//*[@id="page-index"]/div[1]/div[1]/div/div/div[3]/div')  # 出生日期输入框
    ele_ljcs = ('xpath', '//*[@id="page-index"]/div[1]/div[2]/div/div')  # 立即测算按钮
    ele_tips = ('xpath', '/html/body/div[3]/div/span/div/div/div/div')  # 提示框
    ele_wc = ('xpath', '/html/body/div[2]/div[2]/div/div[1]/div[1]/div[3]')  # 完成按钮
    ele_qrzq = ('xpath', '/html/body/div[2]/div[2]/div/div[2]/div[2]/div/button[2]')  # 确认正确按钮
    ele_lqbg=('xpath','//*[@id="page-index"]/div[1]/div[2]/img')  #领取报告按钮
    ele_wxzf = ('xpath', '//*[@id="page-index"]/div[1]/div[3]/div[2]/div[2]/div[3]/div/div[1]/ul/li[2]/div')  # 微信支付
    ele_zfbzf = ('xpath', '//*[@id="page-index"]/div[1]/div[3]/div[2]/div[2]/div[3]/div/div[1]/ul/li[1]/div')  # 支付宝支付
    ele_ljjsnr=('xpath','//*[@id="page-index"]/div[1]/div[3]/div[2]/div[2]/div[3]/div/div[2]/img')  #立即解锁内容按钮
    ele_lsdd = ('xpath', '//*[@id="page-index"]/div/div[2]/div[2]/div[2]/div')  # 历史订单
    ele_ddhsrk = ('xpath', '//*[@id="query"]/div[1]/section/div/div/input')  # 订单号输入框
    ele_lsdjck=("xpath",'//*[@id="orderList"]/li[1]/div[5]')#历史订单点击查看按钮
    ele_ddh = ('xpath', '//*[@id="orderList"]/li/div[3]/div[2]')  # 订单号
    ele_ddtz = ('xpath', '//*[@id="orderList"]/li/div[5]')  # 订单跳转按钮

    def click_ckys(self):
        '''点击查看运势'''
        self.click(self.ele_ckys)

    def input_name(self, text):
        '''输入名字'''
        self.send(self.ele_name, text)

    def choose_birthday(self):
        '''选择出生日期'''
        self.click(self.ele_birthday)
        time.sleep(1)
        self.click(self.ele_wc)
        time.sleep(1)
        self.click(self.ele_qrzq)
        time.sleep(1)

    def click_ljcs(self):
        '''点击立即测算'''
        self.click(self.ele_ljcs)

    def get_tips(self):
        '''获取toast提示'''
        tips = self.get_text(self.ele_tips)
        return tips

    def click_lqbg(self):
        '''点击领取报告'''
        self.click(self.ele_lqbg)

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

    def click_ljjsnr(self):
        '''点击立即解锁内容'''
        self.click(self.ele_ljjsnr)

    def short_name(self):
        '''姓名太短'''
        self.click_ckys()
        self.clear(self.ele_name)
        self.input_name("云")
        self.click_ljcs()
        time.sleep(0.5)

    def long_name(self):
        '''姓名太长'''
        self.click_ckys()
        self.input_name("若云若云若云若云")
        self.click_ljcs()
        time.sleep(0.5)

    def short_english_name(self):
        '''英文姓名太短'''
        self.click_ckys()
        self.clear(self.ele_name)
        self.input_name('s')
        self.click_ljcs()
        time.sleep(0.5)

    def long_english_name(self):
        '''英文姓名太短'''
        self.click_ckys()
        self.clear(self.ele_name)
        self.input_name('ruoyunruoyunruoyun')
        self.click_ljcs()
        time.sleep(0.5)

    def normal_information(self):
        '''正常信息'''
        self.click_ckys()
        self.clear(self.ele_name)
        self.input_name("若云")
        self.choose_birthday()
        self.click_ljcs()
        time.sleep(20)

    def wechat_pay(self):
        '''微信支付'''
        self.normal_information()
        time.sleep(2)
        self.click_lqbg()
        time.sleep(2)
        self.click_wechat_pay()
        time.sleep(2)
        self.click_ljjsnr()
        time.sleep(2)

    def zfb_pay(self):
        '''支付宝支付'''
        self.normal_information()
        time.sleep(2)
        self.click_lqbg()
        time.sleep(2)
        self.click_zfb_pay()
        time.sleep(2)
        self.click_ljjsnr()
        time.sleep(2)

    def lsdd(self):
        '''历史订单'''
        self.click(self.ele_lsdd)

    def dd_wechat_pay(self):
        '''历史订单的微信支付'''
        self.normal_information()
        time.sleep(2)
        self.driver.back()
        time.sleep(1)
        self.driver.back()
        time.sleep(1)
        self.driver.back()
        self.click(self.ele_lsdd)
        # self.send(self.ele_ddhsrk, self.get_text(self.ele_ddh))
        # self.click(self.ele_ddtz)
        self.click(self.ele_lsdjck)
        time.sleep(20)
        js = "var q=document.documentElement.scrollTop=500"
        self.driver.execute_script(js)  # 将页面往下滑动
        self.click_lqbg()
        time.sleep(2)
        self.click_wechat_pay()
        time.sleep(2)
        self.click_ljjsnr()
        time.sleep(2)

    def dd_zfb_pay(self):
        '''历史订单的支付宝支付'''
        self.normal_information()
        time.sleep(2)
        self.driver.back()
        time.sleep(1)
        self.driver.back()
        time.sleep(1)
        self.driver.back()
        self.click(self.ele_lsdd)
        # self.send(self.ele_ddhsrk, self.get_text(self.ele_ddh))
        # self.click(self.ele_ddtz)
        self.click(self.ele_lsdjck)
        time.sleep(20)
        js = "var q=document.documentElement.scrollTop=500"
        self.driver.execute_script(js)  # 将页面往下滑动
        self.click_lqbg()
        time.sleep(2)
        self.click_zfb_pay()
        time.sleep(2)
        self.click_ljjsnr()
        time.sleep(2)