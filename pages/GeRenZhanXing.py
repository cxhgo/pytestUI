from common.base import Base
import time

class Gerenzhanxing(Base):
    '''定义所需要的元素'''
    ele_sex = ("xpath",'//*[@id="page-index"]/div[3]/div[2]/div/div/div[2]/div/ul/li[1]/div[3]/div/input')  #性别选择框
    ele_sex_qd = ("css_selector",'.am-picker-popup-header-right')  #性别的确定按钮
    ele_name = ("xpath", '//*[@id="root"]/div[2]/div[1]/ul/li[1]/div/input') #姓名
    ele_birthday_qd = ("css_selector",'.am-picker-popup-header-right')  #出生日期的确定按钮
    ele_space_qd = ("css_selector",'.am-picker-popup-header-right')  #出生地点的确定按钮
    ele_birthday = ("xpath",'//*[@id="root"]/div[2]/div[1]/ul/li[3]/div/div/span')  #出生日期选择框
    ele_space = ("xpath",'//*[@id="root"]/div[2]/div[1]/ul/li[4]/div/div/span')  #出生地点选择框
    ele_ljcs = ("xpath",'//*[@id="root"]/div[2]/div[1]/div/div/div/img')  #立即测算按钮
    ele_tips = ("xpath",'/html/body/div[3]/div/span/div/div/div/div')  #提示框
    ele_pay_lqbg = ("xpath", '//*[@id="pay"]/div[3]/div[3]/div/img') #支付页-领取报告
    ele_wxzf = ("xpath",'//*[@id="wechat"]')  #微信支付
    ele_zfbzf = ("xpath",'//*[@id="alipay"]')  #支付宝支付
    ele_ylzf = ("xpath",'//*[@id="pay"]/div[3]/div/div[2]/div[2]/ul/li[3]/div[2]/div')  #银联支付
    ele_ppzf = ("xpath",'//*[@id="pay"]/div[3]/div/div[2]/div[2]/ul/li[4]/div[2]/div')  #paypal支付
    ele_ljzf = ("xpath", '//*[@id="pay"]/div[1]/div[2]/div[4]/img') #立即支付
    ele_gengduo = ("xpath",'//*[@id="root"]/div[2]/div[3]/div')  #更多支付方式按钮
    ele_lsdd = ("xpath",'//*[@id="root"]/div[2]/div[3]/div')  #历史订单
    ele_ddh =  ("xpath",'//*[@id="orderList"]/li[1]/div[3]/div[2]')  #订单号
    ele_ddhsrk = ("xpath",'//*[@id="query"]/div[1]/section/div/div/input')  #订单号输入框
    ele_ddtz = ("xpath",'//*[@id="query"]/div[1]/section/button')  #订单跳转
    ele_close = ("xpath",'//*[@id="pay"]/div[1]/div/div[1]/img')  #返回挽留弹窗的关闭按钮

    def choose_birthday(self):
        '''选择出生日期'''
        self.click(self.ele_birthday)
        time.sleep(1)
        self.driver.find_element_by_css_selector('.am-picker-popup-header-right').click()
        time.sleep(1)

    def choose_space(self):
        '''选择出生地点'''
        self.click(self.ele_space)
        time.sleep(1)
        self.driver.find_element_by_css_selector('.am-picker-popup-header-right').click()
        time.sleep(1)

    def input_name(self, text):
        '''输入名字'''
        self.send(self.ele_name, text)

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
        self.click(self.ele_pay_lqbg)
        time.sleep(1)
        self.click(self.ele_wxzf)
        time.sleep(1)
        self.click(self.ele_ljzf)

    def click_zfb_pay(self):
        '''点击支付宝支付'''
        self.click(self.ele_pay_lqbg)
        time.sleep(1)
        self.click(self.ele_zfbzf)
        time.sleep(1)
        self.click(self.ele_ljzf)

    def short_name(self):
        '''输入太短的姓名'''
        self.input_name("云")
        self.click_ljcs()
        time.sleep(0.5)

    def long_name(self):
        '''输入太长的姓名'''
        self.input_name("若云若云若云若云")
        self.click_ljcs()
        time.sleep(0.5)

    def empty_birthday(self):
        '''不填写出生日期'''
        self.input_name("若云")
        self.click_ljcs()
        time.sleep(0.5)

    def empty_space(self):
        '''不填写出生地点'''
        self.input_name("若云")
        self.choose_birthday()
        self.click_ljcs()
        time.sleep(0.5)

    def normal_information(self):
        '''填写正常信息'''
        self.clear(self.ele_name)
        self.input_name("若云")
        self.choose_birthday()
        self.choose_space()
        self.click_ljcs()
        time.sleep(2)

    def wechat_pay(self):
        '''微信支付'''
        self.normal_information()
        time.sleep(20)
        self.click_wechat_pay()
        time.sleep(2)

    def zfb_pay(self):
        '''支付宝支付'''
        self.normal_information()
        time.sleep(20)
        self.click_zfb_pay()
        time.sleep(2)

    def lsdd(self):
        '''历史订单'''
        self.click(self.ele_lsdd)
        time.sleep(5)

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
        self.send(self.ele_ddhsrk, self.get_text(self.ele_ddh))
        self.click(self.ele_ddtz)
        time.sleep(20)
        js = "var q=document.documentElement.scrollTop=700"
        self.driver.execute_script(js)  # 将页面往下滑动
        self.click_wechat_pay()
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
        self.send(self.ele_ddhsrk, self.get_text(self.ele_ddh))
        self.click(self.ele_ddtz)
        time.sleep(20)
        js = "var q=document.documentElement.scrollTop=700"
        self.driver.execute_script(js)  # 将页面往下滑动
        self.click_zfb_pay()
        time.sleep(2)



