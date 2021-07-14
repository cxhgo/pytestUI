# 项目描述

这是web的自动化项目，基于selenium+pytest框架

# 环境准备

1.python3.6
2.pytest4.5.0

依赖包安装
>pip install -r requirement.txt

# 运行用例

>pytest

# 生成报告

生成allure报告

>pytest --alluredir ./allure_report

# pytest.ini配置

pytest.ini配置的描述
'''
[pytest]

--log_cli = 1
;addopts = --alluredir ./allure_report
;testpaths = cases/module
;testfiles = test_*.py

user: ruoyun
'''