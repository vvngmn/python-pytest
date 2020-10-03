
from selenium import webdriver
import pytest

@pytest.mark.feature_webdriver  # $ pytest -m feature_webdriver
def testOpenUrl():   # $ pytest -v -k "OpenUrl"
	try:
		driver = webdriver.Firefox() # 打开浏览器
		driver.get('http://www.baidu.com') # 访问百度
		title = driver.title # 获取百度首页的title
		assert title == '百度一下，你就知道' # 断言
	except AssertionError:

		raise AssertionError('断言失败!')
	driver.quit()
	print("Finished my test: testOpenUrl")
	
def testBaidu():
	driver = webdriver.Firefox() # 打开浏览器
	driver.get('http://www.baidu.com') # 访问百度
	title = driver.title # 获取百度首页的title
	assert title == '百度一下，你就知道' # 断言
	driver.quit()
	print("Finished my test: testBaidu")
