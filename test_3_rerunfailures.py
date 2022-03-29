import time
import pytest
import string

class Test_demo():
    @pytest.mark.demo
    def test_one(self):
        time.sleep(1)
        print("这是第一个用例")
        assert 1 == 1

    @pytest.mark.demo
    @pytest.mark.own
    def test_two(self):
        time.sleep(1)
        print("这是第二个用例")
        assert 1 == 1

    # @pytest.mark.flaky(reruns=2,reruns_delay=1)
    def test_three(self):
        print("这是第三个用例")
        time.sleep(1)
        assert 1 == 1
        # pytest.assume(1 == 2)
        # pytest.assume(2 == 3)
        # pytest.assume(4 == 4)

    def test_two_i(self):
        time.sleep(1)
        print("这是第二个用例")
        assert 1 == 1

    def test_two_p(self):
        time.sleep(1)
        print("这是第二个用例")
        assert 1 == 1

    def test_two3(self):
        time.sleep(1)

        assert 1 == 1

    def test_two4(self):
        time.sleep(1)
        assert 1 == 1

    def test_two5(self):
        time.sleep(1)
        assert 1 == 1

    def test_two6(self):
        time.sleep(1)
        assert 1 == 1

    def test_two7(self):
        time.sleep(1)
        assert 1 == 1

    def test_two8(self):
        time.sleep(1)
        assert 1 == 1

    def test_two9(self):
        time.sleep(1)
        assert 1 == 1

    def test_two10(self):
        time.sleep(1)
        assert 1 == 1


