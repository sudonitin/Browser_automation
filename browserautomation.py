#def savemytime(ids,i,st):
    

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
#it made no difference after adding the below library
from selenium.webdriver.chrome.options import Options
import time
import pyautogui
import PIL.ImageGrab

_chrome_options = Options()
driver = webdriver.Chrome(chrome_options = _chrome_options)
driver.maximize_window()
driver.implicitly_wait(5)


driver.get("https://www.google.co.in/")
search = driver.find_element_by_name("q")
search.send_keys("rait lms")
search.submit()



driver.find_element_by_xpath('//a[contains(text(), "Login")]').click()

user = driver.find_element_by_name("username")
user.send_keys("")#ur username

driver.find_element_by_name("next").click()

driver.implicitly_wait(5)

passw = driver.find_element_by_name("password")
passw.send_keys("")#ur password

driver.find_element_by_id("loginbtn").click()

st = driver.current_url
driver.implicitly_wait(10)
ids = driver.find_elements_by_class_name("launchbutton")
ats = []
for j in ids:
    ats.append(j.get_attribute('href'))
i = 2
while(i<=len(ids)):
    #savemytime(ids,i,st)

    driver.get(ats[i])
    #get all links in this page
    #driver.implicitly_wait(5)
    e = driver.find_elements_by_xpath("//a[@href]")
    a = []
    for j in e:
        a.append(j.get_attribute("href"))#storing all links in a list
    #print(len(a),a[1])
    #if else for each subjects
    if(i==0):
        for k in range(135,193):
            driver.get(a[k])
    elif(i==1):
        for k in range(134,211):
            driver.get(a[k])
    elif(i==2):
        for k in range(50,223):
            driver.get(a[k])
    elif(i==3):
        for k in range(132,207):
            driver.get(a[k])
    elif(i==4):
        for k in range(46,134):
            driver.get(a[k])
    elif(i==5):
        for k in range(122,len(a)+1):
            driver.get(a[k])
            
    #visit the dashboard after each visit
    #driver.get(st)

    
    i = i+1

 
