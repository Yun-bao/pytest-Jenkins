# 改造加减乘除测试用例test_cal.py，使用fixture+conftest.py
# 参数传递、setup\teardown使用fixture
# 使用oytest-ordering插件控制用例执行顺序
# 支持中文编码格式，添加命令行参数使用hook实现
# 生成测试报告截图


# yaml存储数据，并定义get_datas读取参数;用例参数丰富在yaml文件构造
# 针对特别场景，需要捕获异常或者特殊判断，比如浮点数，特别大的数，会存为10e这种
import allure
import pytest





@allure.feature('计算器')
class TestCa:

    @allure.story('相加-整数')
    @pytest.mark.run(order=2)
    def test_addint(self,cal,get_add_datas):
        assert get_add_datas[2] == cal.add(get_add_datas[0],get_add_datas[1])

    @allure.story('相加-浮点数')
    @pytest.mark.run(order=3)
    def test_addfloat(self,cal,get_add_float_datas):
        assert get_add_float_datas[2] == round(cal.add(get_add_float_datas[0],get_add_float_datas[1]),2)

    @allure.story("除法")
    @pytest.mark.last
    def test_div(self,cal,get_div_datas):
        try:
            assert get_div_datas[2] == cal.div(get_div_datas[0],get_div_datas[1])
        except ZeroDivisionError:
            print("除数不能为0")

    @allure.story("相乘-浮点数")
    @pytest.mark.run(order=1)
    def test_mul(self,cal,get_mul_datas):
        assert get_mul_datas[2] == round(cal.mul(get_mul_datas[0],get_mul_datas[1]),2)