import pytest


@pytest.fixture(scope="module", autouse=True)
def setup_teardown():
    print("开始计算")
    yield
    print("结束计算")

