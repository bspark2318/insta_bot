from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from dotenv import load_dotenv
import os
from time import sleep

load_dotenv()
USER_NAME = os.getenv("USER_NAME")
PASSWORD = os.getenv("PASSWORD")

class LoginPage:
    def __init__(self, browser):
        self.browser = browser

    def login(self, username, password):    
        username_input = self.browser,find_element(By.CSS_SELECTOR, "input[name='username']")   
        password_input = self.browser,find_element(By.CSS_SELECTOR, "input[name='password']")
        username_input.send_keys(USER_NAME)
        password_input.send_keys(PASSWORD)
        login_button = self.browser.find_element(By.XPATH, "//button[@type='submit']")
        login_button.click()
        sleep(5)

class HomePage:
    def __init__(self, browser):
        self.browser = browser
        self.browser.get('https://www.instagram.com/')

    def go_to_login_page(self):
        self.browser.find_element(By.XPATH, "//a[text()='Log in']").click()
        sleep(2)
        return LoginPage(self.browser)
    

def test_login_page(browser):
    home_page = HomePage(browser)
    loginPage = home_page.go_to_login_page()
    loginPage.login(USER_NAME, PASSWORD)
    
    errors = browser.find_elements(By.CSS_SELECTOR, '#error_message')
    browser.close()
    
browser = webdriver.Firefox()
browser.implicitly_wait(5)