# content of test_class.py
class TestClass:
    def test_class_one(self):
        x = "this"
        assert "h" in x

    # def test_class_two(self):
    #     x = "hello"
    #     assert hasattr(x, "check")


if __name__ == '__main__':
  pytest.main("-q test_class.py") 
