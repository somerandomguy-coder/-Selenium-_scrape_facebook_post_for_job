from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import re
import string
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utils import preprocess_text, is_valid


url_1 = "https://www.facebook.com/groups/1764357117186212"
url_2 = "https://www.facebook.com/groups/271628854850218"

trigger_words = ["waiter", "waiters", "waitstaff", "waitstaffs", "all-rounder","all-rounders", "runner", "runners", "floor staff", "rsa", "join our team", "requirements", "tuyển dụng", "tuyển nhân viên", "tuyển nam", "tuyển người"]
exclude_words = ["I'm looking for"]


#create chromeoptions instance
options = webdriver.ChromeOptions()

#provide location where chrome stores profiles
options.add_argument(r"--user-data-dir=C:") #write your own chrome profile

#provide the profile name with which we want to open browser
options.add_argument(r'--profile-directory=Default')

#specify where your chrome driver present in your pc
driver = webdriver.Chrome(options=options)

driver.get(url_1)

count = 0
with open(r"src/text.txt", "a") as file:
    while count < 20:
                print("scrolled")
                driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                WebDriverWait(driver, 1000)
                count+=1
    WebDriverWait(driver, 30).until(
    lambda driver: driver.execute_script("return document.readyState") == "complete")
    contents = driver.find_elements(By.XPATH, "//*[contains(@class, 'x11i5rnm') and contains(@class, 'xat24cr') and contains(@class, 'x1mh8g0r') and contains(@class, 'x1vvkbs') and contains(@class, 'xtlvy1s') and contains(@class, 'x126k92a')]")
    for content in contents:
        texts = content.find_elements(By.TAG_NAME, 'div')
        for index, child in enumerate(texts):
            if child.text == "Xem thêm":
                driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", child)
                WebDriverWait(driver, 10).until(lambda driver: child.is_displayed() and child.is_enabled())
                child.click()
    contents = driver.find_elements(By.XPATH, "//*[contains(@class, 'x11i5rnm') and contains(@class, 'xat24cr') and contains(@class, 'x1mh8g0r') and contains(@class, 'x1vvkbs') and contains(@class, 'xtlvy1s') and contains(@class, 'x126k92a')]")
    for content in contents:
        texts = content.find_elements(By.TAG_NAME, 'div')
        for index, child in enumerate(texts):
            print(f"Text inside child div {index + 1}: {child.text}")
            file.write(child.text+"\n")

driver.close()

