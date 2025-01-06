from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def login(usernm, passwrd):
        print("made it here")
        driver = webdriver.Chrome()
        driver.get("https://www.soul-cycle.com/find-a-class/studio/1/")

        loginXpath = "//a[@class='link__StyledAnchor-gvmc2k-0 cUEdex userBadge__StyledLink-sc-8r4hz5-2 kGqEMO']"


        WebDriverWait(driver, 5).until( # wait 5 seconds for this element to pop up
                EC.presence_of_all_elements_located((By.XPATH,loginXpath))
        )

        login = driver.find_element(By.XPATH,loginXpath)
        login.click()
        time.sleep(10)

# WebDriverWait(driver, 5).until( # wait 5 seconds for this element to pop up
#         EC.presence_of_all_elements_located((By.ID, "bigCookie"))
# )
# cookieBut = driver.find_element(By.ID, "bigCookie")
# while True:
#         cookieBut.click()

#         #numCookies = driver.find_element(By.XPATH, "//div[@class='title' and @id='cookies']").text
#         #print(numCookies)
        #print("\n")