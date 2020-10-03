#fixture可以放在单独的测试文件里，如果希望多个测试文件共享fixture，名字必须叫做 conftest.py，将fixture放在其中。
# 使用--setup-show 回溯fixture的执行过程
# $ pytest -v --setup-show  -》show setup of fixtures while executing tests.

import pytest

@pytest.fixture()
def common_fixture():
    print("here is inside common_fixture")
    return 1


@pytest.fixture() # 默认scope='function'：每个function开始和结束各自做一次
def setup_function(request):
    def teardown_function():
        print("[teardown_function called.]")
        print("\n")
    request.addfinalizer(teardown_function)  # 此内嵌函数做teardown工作
    print("\n")
    print('[setup_function called.]')   # `-s` to show the print message

@pytest.fixture(scope='module') # module：一个module的所有function集中只做一次
def setup_module(request):
    def teardown_module():
        print("[teardown_module called.]")
        print("\n")
    request.addfinalizer(teardown_module)
    print("\n")
    print('[setup_module called.]')


@pytest.fixture(scope="session")
def sess_scope():
    print('----------开始session-------------')
    yield
    print('----------结束session-------------')

