# -*- coding:utf-8 -*-
import pytest

class MyFixtures(object):

	@pytest.fixture(scope='function') # function：每个test都运行，默认是function的scope
	def setup_function(self,request):
	    def teardown_function():
	        print("teardown_function called.")
	    request.addfinalizer(teardown_function)  # 此内嵌函数做teardown工作
	    print('setup_function called.')   # `-s` to show the print message

	@pytest.fixture(scope='module') # module：每个module的所有test只运行一次
	def setup_module(self,request):
	    def teardown_module():
	        print("teardown_module called.")
	    request.addfinalizer(teardown_module)
	    print('setup_module called.')


	def test_func(self,text):
		print(text)
