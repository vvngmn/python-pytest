#fixture可以放在单独的测试文件里，如果希望多个测试文件共享fixture，名字必须叫做 conftest.py，将fixture放在其中。
# 使用--setup-show 回溯fixture的执行过程
# $ pytest -v --setup-show  -》show setup of fixtures while executing tests.

# scope参数可以是session， module，class，function； 默认为function
# session 会话级别： 每个session只运行一次，session级别的fixture需要定义到conftest.py中
# module 模块级别：模块里所有的用例执行前执行一次module级别的fixture
# class 类级别 ：每个类执行前都会执行一次class级别的fixture
# function ：这个默认是默认的模式，函数级别的，每个测试用例执行前都会执行一次function级别的fixture

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

