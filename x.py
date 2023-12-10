import time
from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class Twitter:

    def __init__(self):

        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)

        self.driver = webdriver.Chrome(options=options)
        self.driver.set_window_size(1700, 1000)

    def log_in(self, user, password):
        self.driver.get('https://twitter.com/')
        time.sleep(5)
        self.driver.find_element(By.XPATH, '(//div[@role="button"])[1]').click()
        self.driver.find_element(By.XPATH, '//a[@data-testid="loginButton"]').click()
        time.sleep(5)
        self.driver.find_element(By.CSS_SELECTOR, 'input[autocomplete="username"]').send_keys(user)
        self.driver.find_element(By.XPATH, '(//div[@role="button"])[3]').click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, '//input[@name="password"]').send_keys(password)
        self.driver.find_element(By.XPATH, '(//div[@role="button"])[3]').click()
        wait = WebDriverWait(self.driver, 15)
        try:
            logged = EC.url_contains("/home")
            wait.until(logged)
        except:
            print("Not yet logged")
            time.sleep(10)

    def post_on_x(self, desired_d_speed, desired_u_speed, my_d_speed, my_u_speed , target_user):
        textarea = self.driver.find_element(By.XPATH, '//div[@class="DraftEditor-root"]')
        textarea.click()
        time.sleep(2)
        textarea.send_keys(f"Hey, why is my speed {my_d_speed}/{my_u_speed}, when I pay for {desired_d_speed}/{desired_u_speed}? @{target_user}")
        time.sleep(2)
        self.driver.find_element(By.XPATH, '(//div[@data-testid="TypeaheadUser"])[1]').click()
        #Here I'd click post button

