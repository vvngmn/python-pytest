# -*- coding:utf-8 -*-
import sys, os
# sys.path.append(os.path.join('..', 'fixtures'))
import pytest
from libs.MyFixtures import *

######################### define fixures
# @pytest.fixture(scope='function') # function：每个test都运行，默认是function的scope
# def setup_function(request):
#     def teardown_function():
#         print("teardown_function called.")
#     request.addfinalizer(teardown_function)  # 此内嵌函数做teardown工作
#     print('setup_function called.')   # `-s` to show the print message

# @pytest.fixture(scope='module') # module：每个module的所有test只运行一次
# def setup_module(request):
#     def teardown_module():
#         print("teardown_module called.")
#     request.addfinalizer(teardown_module)
#     print('setup_module called.')
#########################

class TestFixtures(MyFixtures):

    setmodule = MyFixtures.setup_module


    @pytest.mark.feature1 # $pytest -v -m "feature1" pytest1.py (need prepare pytest.ini)
    def test_1(setup_function):
        print('~~~~~Test_1 called.')

    @pytest.mark.feature2
    @pytest.mark.fixture_feature2
    def test_2(setmodule):
        assert "ok"
        print('~~~~~Test_2 called.')

    @pytest.mark.feature3
    def test_3(setup_module):
        print('~~~~~Test_3 called.')
        assert 2==1+1              # 通过assert断言确认测试结果是否符合预期

if __name__=='__main__':
    print("start")
    c = TestFixtures

