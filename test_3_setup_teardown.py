import pytest

def setup_module():
    print("SET UP:在模块开始的时候的执行")

def teardown_module():
    print("TEAR DOWN:在模块结束的时候的执行")

def setup_function():
    print("不在类里面测试执行的开始时候执行")

def teardown_function():
    print("不在类里面测试执行的结束时候执行")

def test_three():
    print("test three")

def test_four():
    print("test four")

class Test_demo():
    def setup_class(self):
        print("执行类用例开始的时候执行")

    def teardown_class(self):
        print("执行类用例结束的时候执行")

    def setup_method(self):
        print("执行方法开始的时候执行")

    def teardown_method(self):
        print("执行方法结束的时候执行")

    def test_one(self):
        print("test one")

    def test_two(self):
        print("test two")
