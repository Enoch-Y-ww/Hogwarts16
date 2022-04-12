'''
使用序列化cookie的方式 登录企业微信，完成添加联系人，加上断言验证
'''
from time import sleep
import yaml
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestGetCookies():
	def test_getcookies(self):
		option = webdriver.ChromeOptions()
		option.debugger_address = '127.0.0.1:9222'
		driver = webdriver.Chrome(options=option)
		driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
		driver.find_element(By.ID, "menu_contacts").click()
		sleep(2)
		cookies = driver.get_cookies()
		print(cookies)
		with open("data.yaml", "w", encoding="UTF-8") as f:
			yaml.dump(cookies, f)
		
class TestLoginWithCookies():
	def test_loginwithcookies(self):
		driver = webdriver.Chrome()
		driver.implicitly_wait(5)
		driver.maximize_window()
		driver.get("https://work.weixin.qq.com/wework_admin/loginpage_wx")
		with open("data.yaml", encoding="UTF-8") as f:
			cookies = yaml.safe_load(f)
			for cookie in cookies:
				driver.add_cookie(cookie)
		driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
		driver.find_element(By.ID, "menu_contacts").click()
		sleep(2)
		# driver.find_element(By.XPATH, '//*[@id="js_contacts52"]/div/div[2]/div/div[2]/div[3]/div[1]/a[1]').click()
		driver.find_element(By.LINK_TEXT, "添加成员").click()
		input_name = "王八"
		driver.find_element(By.ID, "username").send_keys(input_name)
		driver.find_element(By.ID, "memberAdd_acctid").send_keys("154789")
		driver.find_element(By.ID, "memberAdd_biz_mail").clear()
		driver.find_element(By.ID, "memberAdd_biz_mail").send_keys("wangba123")
		driver.find_element(By.ID, "memberAdd_mail").send_keys("452840569@qq.com")
		driver.find_element(By.LINK_TEXT, "保存").click()
		sleep(2)
		name = driver.find_element(By.XPATH, '//*[@id="member_list"]/tr/td[2]').get_attribute("title")
		assert input_name in name
		sleep(2)
		driver.quit()
		