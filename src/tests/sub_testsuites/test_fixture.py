# -*- coding:utf-8 -*-
# import sys, os
# sys.path.append(os.path.join('..', 'fixtures'))
import pytest
# from MyFixtures import *

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

# class TestFixtures():

    # func = MyFixtures.test_func()


@pytest.mark.test_function # $pytest -v -m "feature1" pytest1.py (need prepare pytest.ini)
def test_1_1(setup_function):
    print('~~~~~Test_1—1 called.')

@pytest.mark.test_function 
def test_1_2(setup_function):
    print('~~~~~Test_1—2 called.')

@pytest.mark.test_function 
def test_1_3():
    print('~~~~~Test_1—3 called.')


@pytest.mark.test_module
def test_2_1(setup_module):
    print(type(setup_module))
    assert "ok" # 通过assert return true or false
    print('~~~~~Test_2_1 called.')

@pytest.mark.test_module
def test_2_2(setup_module):
    print(type(setup_module))
    assert "ok" # 通过assert return true or false
    print('~~~~~Test_2_2 called.')

@pytest.mark.test_module
def test_2_3(setup_module):
    print(type(setup_module))
    assert "ok" # 通过assert return true or false
    print('~~~~~Test_2_3 called.')


@pytest.mark.test_session
def test_3_1(sess_scope):
    print(type(sess_scope))
    assert "ok" 
    print('~~~~~Test_3_1 called.')            

@pytest.mark.test_session
def test_3_2(sess_scope):
    print(type(sess_scope))
    assert "ok" 
    print('~~~~~Test_3_2 called.') 

@pytest.mark.test_session
def test_3_3(sess_scope):
    print(type(sess_scope))
    assert "ok" 
    print('~~~~~Test_3_3 called.') 


# if __name__=='__main__':
#     print("start")
#     c = TestFixtures

