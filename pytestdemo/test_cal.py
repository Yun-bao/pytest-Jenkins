# yaml存储数据，并定义get_datas读取参数;用例参数丰富在yaml文件构造
# 针对特别场景，需要捕获异常或者特殊判断，比如浮点数，特别大的数，会存为10e这种
import pytest
import yaml

from pytestdemo.Calculator import Calculator


def get_datas():
    with open("../datas/caldata.yaml",encoding='utf-8') as f:
        datas = yaml.safe_load(f)
        print(datas)
    return datas

class TestCa:
    def setup_class(self):
        print("setup")
        self.calc = Calculator()
    def teardown_class(self):
        print("teardown_class")

    def setup(self):
        print("计算开始")
        self.cal = Calculator()

    def teardown(self):
        print("计算结束")

    @pytest.mark.parametrize('x,y,expect',get_datas()['datas'],ids=get_datas()['ids'])
    def test_addint(self,x,y,expect):
        assert expect == self.cal.add(x,y)

    @pytest.mark.parametrize('x,y,expect', get_datas()['float_datas'], ids=get_datas()['float_ids'])
    def test_addfloat(self,x,y,expect):
        assert expect == round(self.cal.add(x,y),2)

    @pytest.mark.parametrize('x,y,expect',[[1,0,0],[1,2,0.5]],ids=['0','float'])
    def test_div(self,x,y,expect):
        try:
            assert expect == self.cal.div(x,y)
        except ZeroDivisionError:
            print("除数不能为0")

    @pytest.mark.parametrize('x,y,expect', get_datas()['float_muldatas'], ids=get_datas()['float_mulids'])
    def test_mul(self, x, y, expect):
        assert expect == round(self.cal.mul(x, y),2)