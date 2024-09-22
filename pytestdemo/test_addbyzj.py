import pytest
import yaml

from pytestdemo.Calculator import Calculator


class TestCalculator:
    def setup_class(self):
        print("setup")
        self.calc = Calculator()
    def teardown_class(self):
        print("teardown_class")

    def setup(self):
        print("计算开始")

    def teardown(self):
        print("计算结束")

    @pytest.mark.parametrize('a,b,expect,operation', yaml.safe_load(open("../datas/Cal.yaml",encoding='utf-8')))
    def test_calculations(self,a,b,expect,operation):
            if operation == 'add':
                assert self.calc.add(a,b) == expect
            if operation == 'mul':
                assert self.calc.mul(a,b) == expect
            if operation == 'sub':
                assert self.calc.sub(a,b) == expect
            if operation == 'div':
                assert self.calc.div(a,b) == expect