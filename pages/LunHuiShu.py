from common.base import Base
import time

class Lunhuishu(Base):
    '''定义所需要的元素'''
    ele_sy_ljcs = ("xpath", '//*[@id="root"]/div[2]/div[2]/div/img') # 首页立即测算
    ele_name = ("xpath",'//*[@id="root"]/div[1]/div[1]/div[1]/div/input')     #姓名输入框
    ele_boy = ("xpath", "//*[@id='root']/div[3]/div[2]/div[1]/div[2]/div/div[1]")  # 性别为男
    ele_girl = ("xpath", "//*[@id='root']/div[3]/div[2]/div[1]/div[2]/div/div[2]")  # 性别为女
    ele_birthday = ("xpath", '//*[@id="root"]/div[1]/div[1]/div[3]/div')  # 出生日期选择框
    ele_ljcs = ("xpath", '//*[@id="root"]/div[1]/div[2]/div/img')  # 立即测算按钮
    ele_tips = ("xpath", '/html/body/div[4]/div/span/div/div/div/div')  # 姓名为空时的提示
    ele_wc = ("xpath", '/html/body/div[3]/div[2]/div/div[1]/div[1]/div[3]')  # 完成按钮
    ele_qrzq = ("xpath", '/html/body/div[3]/div[2]/div/div[2]/div[2]/div/button[2]')  # 确认正确按钮
    ele_zfy_lqbg = ("xpath", '//*[@id="root"]/div[1]/div[2]/img') # 支付页领取报告
    ele_gdzf = ("xpath","//*[@id='pay']/div[3]/div/div[2]/div")         #更多方式按钮
    ele_wxzf = ("xpath", '//*[@id="root"]/div[1]/div[3]/div[2]/div[2]/div[2]/div/div[1]/div[2]/label')  # 微信支付按钮
    ele_zfbzf = ("xpath", '//*[@id="root"]/div[1]/div[3]/div[2]/div[2]/div[2]/div/div[1]/div[1]/label')  # 支付宝支付按钮
    ele_zfy_ljjs = ("xpath", '//*[@id="root"]/div[1]/div[3]/div[2]/div[2]/div[2]/div/div[2]/img') # 支付页-立即解锁
    ele_lsdd = ("xpath", '//*[@id="root"]/div[2]/div[2]/div/div[2]/div')  # 查询历史订单按钮
    ele_ddh = ("xpath", '//*[@id="orderList"]/li[1]/div[3]/div[2]')  # 订单号
    ele_lsdjck=("xpath",'//*[@id="orderList"]/li[1]/div[5]')#历史订单点击查看按钮
    ele_hbmb =("xpath",'//*[@id="root"]/div[1]/div/button')#红包领取按钮
    #ele_guanbi = (By.XPATH, "//*[@id='page-pay']/section/div[1]/div[2]/div[1]")  # 返回弹窗的关闭按钮
    ele_ddhsrk = ("xpath", '//*[@id="query"]/div[1]/section/div/div/input')  # 订单号输入框
    ele_ddtz = ("xpath", '//*[@id="query"]/div[1]/section/button')  # 订单跳转按

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

    def get_url(self):
        '''获取当前页面的url'''
        current_url = self.driver.current_url
        return current_url

    def click_wechat_pay(self):
        '''点击微信支付'''
        self.click(self.ele_zfy_lqbg)
        time.sleep(1)
        self.click(self.ele_wxzf)
        time.sleep(1)
        self.click(self.ele_zfy_ljjs)

    def click_zfb_pay(self):
        '''点击支付宝支付'''
        self.click(self.ele_zfy_lqbg)
        time.sleep(1)
        self.click(self.ele_zfbzf)
        time.sleep(1)
        self.click(self.ele_zfy_ljjs)


    def empty_name(self):
        '''不填写姓名'''
        self.clear(self.ele_name)
        self.click_ljcs()
        time.sleep(0.3)

    def short_name(self):
        '''名字太短'''
        self.click(self.ele_sy_ljcs)
        self.clear(self.ele_name)
        self.input_name("云")
        self.click_ljcs()
        time.sleep(0.5)

    def long_name(self):
        '''名字太长'''
        self.click(self.ele_sy_ljcs)
        self.clear(self.ele_name)
        self.input_name("若云若云若云若云")
        self.click_ljcs()
        time.sleep(0.5)

    def short_english_name(self):
        '''英文名字太短'''
        self.click(self.ele_sy_ljcs)
        self.clear(self.ele_name)
        self.input_name('s')
        self.click_ljcs()
        time.sleep(0.5)

    def long_english_name(self):
        '''英文名字太长'''
        self.click(self.ele_sy_ljcs)
        self.clear(self.ele_name)
        self.input_name('ruoyunruoyunruoyun')
        self.click_ljcs()
        time.sleep(0.5)

    def normal_information(self):
        '''正常信息'''
        self.click(self.ele_sy_ljcs)
        self.clear(self.ele_name)
        self.input_name('若云')
        time.sleep(1)
        self.choose_birthday()
        time.sleep(1)
        self.click_ljcs()
        time.sleep(2)

    def wechat_pay(self):
        '''微信支付'''
        self.normal_information()
        time.sleep(30)
        self.click_wechat_pay()
        time.sleep(2)

    def zfb_pay(self):
        '''支付宝支付'''
        self.normal_information()
        time.sleep(30)
        self.click_zfb_pay()
        time.sleep(2)


    def lsdd(self):
        '''历史订单'''
        self.click(self.ele_lsdd)
        time.sleep(1)

    def dd_wechat_pay(self):
        '''历史订单的微信支付'''
        time.sleep(1)
        self.normal_information()
        self.driver.back()
        time.sleep(1)
        self.driver.back()
        time.sleep(1)
        self.driver.back()
        time.sleep(1)
        self.driver.back()
        self.click(self.ele_lsdd)
        # self.send(self.ele_ddhsrk, self.get_text(self.ele_ddh))
        # self.click(self.ele_ddtz)
        self.click(self.ele_lsdjck)
        self.click(self.ele_hbmb)
        time.sleep(3)
        self.driver.back()
        time.sleep(30)
        js = "var q=document.documentElement.scrollTop=500"
        self.driver.execute_script(js)  # 将页面往下滑动
        self.click_wechat_pay()
        time.sleep(2)

    def dd_zfb_pay(self):
        '''历史订单的支付宝支付'''
        time.sleep(1)
        self.normal_information()
        time.sleep(2)
        self.driver.back()
        time.sleep(1)
        self.driver.back()
        time.sleep(1)
        self.driver.back()
        time.sleep(1)
        self.driver.back()
        self.click(self.ele_lsdd)
        # self.send(self.ele_ddhsrk, self.get_text(self.ele_ddh))
        # self.click(self.ele_ddtz)
        self.click(self.ele_lsdjck)
        self.click(self.ele_hbmb)
        time.sleep(3)
        self.driver.back()
        time.sleep(30)
        js = "var q=document.documentElement.scrollTop=500"
        self.driver.execute_script(js)  # 将页面往下滑动
        self.click_zfb_pay()
        time.sleep(2)