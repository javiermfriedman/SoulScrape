from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def login(username, passwrd):
    driver = webdriver.Chrome()
    driver.get("https://www.soul-cycle.com/find-a-class/studio/1/")

    loginXpath = "//a[@class='link__StyledAnchor-gvmc2k-0 cUEdex userBadge__StyledLink-sc-8r4hz5-2 kGqEMO']"

    # Wait for the login button and click it
    WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, loginXpath))
    )
    login_btn = driver.find_element(By.XPATH, loginXpath)
    login_btn.click()

    # Enter email
    WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, '//input[contains(@class, "floating__input")]'))
    )
    login_email = driver.find_element(By.XPATH, '//input[contains(@class, "floating__input")]')
    login_email.send_keys(username + Keys.ENTER)

    # Enter password
    login_passwrd = driver.find_element(By.XPATH, '//input[@id="password-input"]')
    login_passwrd.send_keys(passwrd + Keys.ENTER)

    # Click the next button
    next_button_1 = driver.find_element(By.XPATH, '//button[@id="handle-login"]')
    next_button_1.click()

    try:
        # Wait for the reCAPTCHA element for 5 seconds
        recaptcha_element = WebDriverWait(driver, 3).until(
            EC.presence_of_element_located((By.XPATH, '//span[@id="recaptcha-anchor"]'))
        )
        # If found, click the reCAPTCHA
        recaptcha_element.click()
        print("reCAPTCHA found and clicked.")
    except Exception as e:
        # Handle case where reCAPTCHA does not appear
        print("reCAPTCHA not found, proceeding without it.")

    # Wait for some time to observe the result (optional)
    driver.get("https://www.soul-cycle.com/find-a-class/studio/1/")
    time.sleep(20)

    # Quit the browser
    driver.quit()
