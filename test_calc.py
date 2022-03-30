import allure
import pytest
import yaml
from pythoncode.calculator import Calculator


def get_add():
    with open("./data_calc.yaml") as f:
        datas = yaml.safe_load(f)
        return datas


@allure.feature("数据运算验证")
class TestOfCalc:
    calc = Calculator()

    @allure.story("加法验算：")
    @allure.title("加法运算验证")
    @pytest.mark.parametrize("a, b, expected", get_add()['add'])          # 数据驱动
    # @pytest.mark.parametrize("a, b, expected",[
    #     (1,3,4),(-3,0,-3),(-3,-2,-5),(-2,3,1),(1000,2000,3000)
    # ])
    def test_add(self, a, b, expected):
        assert expected == self.calc.add(a, b)

    @allure.story("减法验算：")
    @allure.title("减法运算验证")
    @pytest.mark.parametrize("a, b, expected", get_add()['sub'])          # 数据驱动
    # @pytest.mark.parametrize("a, b, expected", [
    #     (1, 3, -2), (-3, 0, -3), (-3, -2,-1), (-2, -3, 1), (2000, 1000, 1000)
    # ])
    def test_sub(self, a, b, expected):
        assert expected == self.calc.sub(a, b)

    @allure.story("乘法验算：")
    @allure.title("乘法运算验证")
    @pytest.mark.parametrize("a, b, expected", get_add()['mul'])           # 数据驱动
    # @pytest.mark.parametrize("a, b, expected", [
    #     (1, 3, 3), (-3, 0, 0), (-3, -2, 6), (-2, 3, -6), (4, 0, 0)
    # ])
    def test_mul(self, a, b, expected):
        assert expected == self.calc.mul(a, b)

    @pytest.mark.run(order=1)
    @allure.story("除法验算：")
    @allure.title("除法运算验证")
    @pytest.mark.parametrize("a, b, expected", get_add()['div'])           # 数据驱动
    # @pytest.mark.parametrize("a, b, expected", [
    #     (-6,-2,3), (-3, 0, 0), (-3, 1, -3), (15, -3, -5), (100, 4, 25)
    # ])
    def test_div(self, a, b, expected):
        if b == 0:
            print("b不能等于0")
        else:
            assert expected == self.calc.div(a, b)

