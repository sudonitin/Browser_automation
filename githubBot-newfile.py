import strgen
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
import os

chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument('--no-sandbox')
driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)

#_chrome_options = Options() for local
#driver = webdriver.Chrome(chrome_options = _chrome_options) for local
driver.implicitly_wait(5)

driver.get("https://github.com/login")
username = driver.find_element_by_id("login_field")
username.send_keys("globefire")
password = driver.find_element_by_id("password")
password.send_keys("iammythical123")
signin = driver.find_element_by_name("commit")
signin.submit()

#driver.get("https://github.com/globefire/Goals")
#driver.implicitly_wait(5)

#driver.find_element_by_css_selector("#readme > div.Box-header.d-flex.flex-items-center.flex-justify-between.px-2 > div > a > svg").click()

#creating a new file
driver.get("https://github.com/globefire/Goals/new/master")
driver.implicitly_wait(5)
#driver.find_element_by_xpath('//*[@id="js-repo-pjax-container"]/div[2]/div[1]/div[3]/div[2]/form/button').click()
#readmeIp = driver.find_element_by_name("filename")

readmeIp = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.NAME, "filename"))
)

a = strgen.StringGenerator("[\d\w]{3}").render()
readmeIp.send_keys(a)

driver.find_element_by_id("submit-file").click()

driver.close()
driver.quit()
