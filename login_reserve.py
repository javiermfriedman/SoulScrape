from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.get("https://orteil.dashnet.org/cookieclicker/")


WebDriverWait(driver, 5).until( # wait 5 seconds for this element to pop up
        EC.presence_of_all_elements_located((By.XPATH,"//div[text()='English']"))
)

language = driver.find_element(By.XPATH,"//div[text()='English']")
language.click()

WebDriverWait(driver, 5).until( # wait 5 seconds for this element to pop up
        EC.presence_of_all_elements_located((By.ID, "bigCookie"))
)
cookieBut = driver.find_element(By.ID, "bigCookie")
while True:
        cookieBut.click()

        #numCookies = driver.find_element(By.XPATH, "//div[@class='title' and @id='cookies']").text
        #print(numCookies)
        #print("\n")