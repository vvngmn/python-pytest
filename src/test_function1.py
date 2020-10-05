# -*- coding:utf-8 -*-
import pytest, sys

# 用yield关键字呼唤teardown操作, 替代fixture的setup函数中 request.addfinalizer(teardown_module)
@pytest.fixture(scope='module')
def login():
    print(" ～～～～～ setup ～～～～～")
    yield
    print(" ～～～～～ tear down ～～～～～ ")

def test1(login):
    print("操作1")
    print("---------------------------------------------------")

def test_negative_test(login):
    try:
        print("操作反向测试..")
        raise Exception("expect inside test fail!")
        print("---------------------------------------------------")
    except Exception as err: 
        assert ("expect inside test" in str(err))

def test2(login):
    print("操作2")
    print("---------------------------------------------------")



if __name__=="__main__":
    pytest.main(["-sv", sys.argv[0]])
