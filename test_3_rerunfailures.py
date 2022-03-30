import time
import pytest


class TestOfDemo:
    @pytest.mark.demo
    def test_one_1(self):
        time.sleep(1)
        print("这是第一个用例")
        assert 1 == 1

    @pytest.mark.demo
    @pytest.mark.own
    def test_one_2(self):
        time.sleep(1)
        print("这是第二个用例")
        assert 1 == 1

    # @pytest.mark.flaky(reruns=2,reruns_delay=1)
    def test_one_3(self):
        print("这是第三个用例")
        time.sleep(1)
        assert 1 == 1
        # pytest.assume(1 == 2)
        # pytest.assume(2 == 3)
        # pytest.assume(4 == 4)

    def test_one_4(self):
        time.sleep(1)
        print("这是第二个用例")
        assert 1 == 1

    def test_one_5(self):
        time.sleep(1)
        print("这是第二个用例")
        assert 1 == 1

    def test_one_6(self):
        time.sleep(1)

        assert 1 == 1

    def test_one_7(self):
        time.sleep(1)
        assert 1 == 1

    def test_one_8(self):
        time.sleep(1)
        assert 1 == 1

    def test_one_9(self):
        time.sleep(1)
        assert 1 == 1

    def test_one_10(self):
        time.sleep(1)
        assert 1 == 1

    def test_one_11(self):
        time.sleep(1)
        assert 1 == 1

    @pytest.mark.run(order=2)
    def test_one_12(self):
        time.sleep(1)
        assert 1 == 1

    @pytest.mark.run(order=1)
    def test_one_13(self):
        time.sleep(1)
        assert 1 == 1
