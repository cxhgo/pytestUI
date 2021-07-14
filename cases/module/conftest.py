import pytest

# def pytest_hook():
#     pass
#
# print("xxxxxxxx")
#
# if __name__ == '__main__':
#     def pytest_hook():
#         print("重写上面的函数")
#     pytest_hook()

def pytest_addoption(parser):
    parser.addoption(
        "--host", action="store", default="test", help="option test or uat or pre"
    )
    parser.addini(
        name="user", type=None, default="admin", help="pytest.ini: test user"
    )

# 读取命令行参数
@pytest.fixture()
def  host_env(request):
    env = request.config.getoption("--host")
    if env == "test":
        url = "http://49.235.92.12:8200/"
    elif env == "uat":
        url = "https://www.baidu.com/"
    else:
        url = "http://49.235.92.12:8200/"
    server = getattr(request.module, "web_server", url)
    return server

def env(pytestconfig):
    env = pytestconfig.getoption("--host")

@pytest.fixture(scope="session", autouse=True)
def get_ini(pytestconfig):
    cmdopts = pytestconfig.getini("addopts")
    print("读取ini配置的内容：%s"% cmdopts)

@pytest.fixture(scope="session", autouse=True)
def get_user(pytestconfig):
    user = pytestconfig.getini("user")
    print("读取到ini文件的user：%s" % user)
