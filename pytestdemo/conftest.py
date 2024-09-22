import pytest
import yaml

from Calculator import Calculator


@pytest.fixture()
def cal():
    print("计算开始")
    cal = Calculator()
    yield cal
    print("计算结束")


def get_datas_c():
    with open("../datas/caldata.yaml",encoding='utf-8') as f:
        datas = yaml.safe_load(f)
        print(datas)
    return datas

@pytest.fixture(params=get_datas_c()['float_muldatas'],ids=get_datas_c()['float_mulids'])
def get_mul_datas(request):
    return request.param

@pytest.fixture(params=get_datas_c()['datas'],ids=get_datas_c()['ids'])
def get_add_datas(request):
    return request.param

@pytest.fixture(params=get_datas_c()['float_datas'],ids=get_datas_c()['float_ids'])
def get_add_float_datas(request):
    return request.param

@pytest.fixture(params=get_datas_c()['divdatas'],ids=get_datas_c()['divids'])
def get_div_datas(request):
    return request.param

# def test_mul_datas(get_mul_datas):
#     print(get_mul_datas)

# 钩子函数（hook函数），所有用例执行前收集

def pytest_collection_modifyitems(session, config, items:list):
    print("这是收集所有测试用例的方法")
    print(items)
    items.reverse()
    for item in items:
        item.name = item.name.encode('utf-8').decode('unicode-escape')
        item._nodeid = item.nodeid.encode('utf-8').decode('unicode-escape')
        if 'mul' in item.name:
            item.add_marker(pytest.mark.mul)
        if 'div' in item.name:
            item.add_marker(pytest.mark.div)