import strgen
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

_chrome_options = Options()
driver = webdriver.Chrome(chrome_options = _chrome_options)
driver.implicitly_wait(5)

driver.get("https://github.com/login")
username = driver.find_element_by_id("login_field")
username.send_keys("type your username here")
password = driver.find_element_by_id("password")
password.send_keys("type your password here")
signin = driver.find_element_by_name("commit")
signin.submit()

driver.get("repo link here, readme.md is prerequisite")
driver.find_element_by_xpath('//*[@id="readme"]/div[1]/div').click()

readmeIp = driver.find_element_by_name("filename")
a = strgen.StringGenerator("[\d\w]{3}").render()
readmeIp.send_keys(a)

driver.find_element_by_id("submit-file").click()

driver.close()
driver.quit()
