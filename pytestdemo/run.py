# coding=gbk
import os
import pytest

pytest.main([])

os.system("allure generate ./allure_result -o ./allure_report --clean")