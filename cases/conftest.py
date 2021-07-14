from selenium import webdriver
import pytest
from selenium.webdriver.chrome.options import Options
import platform
from pages.BaZiHeHun import Bazihehun
from pages.BaZiLiuNian import Baziliunian
from pages.BaZiYinYuan import Baziyinyuan
from pages.GeRenZhanXing import Gerenzhanxing
from pages.LunHuiShu import Lunhuishu
from pages.ShiNianDaYun import Shiniandayun
from pages.ShiYeXiangPi import Shiyexiangpi
from pages.SongShaoGuangYunCheng import Songshaoguangyuncheng
from pages.YiShengCaiYun import Yishengcaiyun
from pages.ZhanWeiZhongJingPi import Zhanweizhongjingpi
from pages.JingPinQianShiYinYuan import Jingpinqianshiyinyuan
from pages.NiuNianYunCheng import Niunianyuncheng


@pytest.fixture(scope="session", name="driver")
def browser():
    '''定义全局driver'''
    if platform.system() == 'Windows':
        # windows系统
        # _driver = webdriver.Chrome()

        # 无界面模式
        chrome_options = Options()
        chrome_options.add_argument('--window-size=1920,1080')  # 设置当前窗口的宽度和高度
        chrome_options.add_argument('--headless')
        _driver = webdriver.Chrome(options=chrome_options)


    else:
        # linux启动
        chrome_options = Options()
        chrome_options.add_argument('--window-size=1920,1080')  # 设置当前窗口的宽度和高度
        chrome_options.add_argument('--no-sandbox')  # 解决DevToolsActivePort文件不存在报错问题
        chrome_options.add_argument('--disable-dev-shm-usage')
        chrome_options.add_argument('--disable-gpu')   # 禁用GPU硬件加速。如果软件渲染器没有就位，则GPU进程将不会启动。
        chrome_options.add_argument('--headless')  # 无界面

        # _driver = webdriver.Chrome()
        _driver = webdriver.Chrome(chrome_options=chrome_options)

    yield _driver
    # quit是退出浏览器
    _driver.quit()



@pytest.fixture(scope="session")
def base_url():
    return "https://cs.lingbz.com"


@pytest.fixture(scope="session")
def bzhh(driver, base_url):
    bzhh = Bazihehun(driver, base_url)
    return bzhh

@pytest.fixture(scope="session")
def bzln(driver, base_url):
    bzln = Baziliunian(driver, base_url)
    return bzln

@pytest.fixture(scope="session")
def bzyy(driver, base_url):
    bzyy = Baziyinyuan(driver, base_url)
    return bzyy

@pytest.fixture(scope="session")
def grzx(driver, base_url):
    grzx = Gerenzhanxing(driver, base_url)
    return grzx

@pytest.fixture(scope="session")
def lhs(driver, base_url):
    lhs = Lunhuishu(driver, base_url)
    return lhs

@pytest.fixture(scope="session")
def sndy(driver, base_url):
    sndy = Shiniandayun(driver, base_url)
    return sndy

@pytest.fixture(scope="session")
def syxp(driver, base_url):
    syxp = Shiyexiangpi(driver, base_url)
    return syxp

@pytest.fixture(scope="session")
def ssgyc(driver, base_url):
    ssgyc = Songshaoguangyuncheng(driver, base_url)
    return ssgyc

@pytest.fixture(scope="session")
def yscy(driver, base_url):
    yscy = Yishengcaiyun(driver, base_url)
    return yscy

@pytest.fixture(scope="session")
def zwzjp(driver, base_url):
    zwzjp = Zhanweizhongjingpi(driver, base_url)
    return zwzjp
    
@pytest.fixture(scope="session")
def jpqsyy(driver,base_url):
    jpqsyy=Jingpinqianshiyinyuan(driver,base_url)
    return jpqsyy
    
@pytest.fixture(scope="session")
def nnyc(driver,base_url):
    nnyc=Niunianyuncheng(driver,base_url)
    return nnyc