#fixture可以放在单独的测试文件里，如果希望多个测试文件共享fixture，可以在公共目录下新建一个conftest.py，将fixture放在其中。
# 使用--setup-show 回溯fixture的执行过程
# $ pytest -v --setup-show test_demo8.py

import pytest

@pytest.fixture()
def common_fixture():
    print("here is inside common_fixture")
    return 1


@pytest.fixture(scope='function') # function：每个test都运行，默认是function的scope
def setup_function(request):
    def teardown_function():
        print("[teardown_function called.]")
    request.addfinalizer(teardown_function)  # 此内嵌函数做teardown工作
    print('[setup_function called.]')   # `-s` to show the print message

@pytest.fixture(scope='module') # module：每个module的所有test只运行一次
def setup_module(request):
    def teardown_module():
        print("[teardown_module called.]")
    request.addfinalizer(teardown_module)
    print('[setup_module called.]')


@pytest.fixture(scope='module')
def test_fixture():
    print("here inside test_fixture")
    return " --- hello!!"
