import pytest

# class TestClassDemoInstance:
@pytest.mark.feature1
def test_one():
	assert "ok"

@pytest.mark.feature2
def test_two():
	assert "ok"




# class TestClassDemoInstance:
# 	@pytest.mark.feature2
# 	def test_two(self):
# 	    assert "ok"



# if __name__ == '__main__':
#   pytest.main("-q test_class_demo.py") 