import time
from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SpeedTest:

    def __init__(self):

        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)

        self.driver = webdriver.Chrome(options=options)
        self.driver.set_window_size(1700, 1000)


    def getSpeed(self):

        self.driver.get("https://www.speedtest.pl/")
        time.sleep(1)

        cookie_btn= self.driver.find_element(By.CSS_SELECTOR, 'button[aria-label="OK, przejdź do strony"]')
        cookie_btn.click()

        wait = WebDriverWait(self.driver, 80)

        time.sleep(2)
        start_btn = self.driver.find_element(By.CSS_SELECTOR, 'div[class="label flex m-auto"]')
        start_btn.click()

        try:
            test_finished = EC.url_contains("/wynik")
            wait.until(test_finished)
            d_speed = self.driver.find_element(By.XPATH, "(//*[contains(@class, 'value-wrapper')])[1]")
            u_speed = self.driver.find_element(By.XPATH, "(//*[contains(@class, 'value-wrapper')])[2]")
            d_speed_val = float(d_speed.text)
            u_speed_val = float(u_speed.text)
            print(d_speed_val, u_speed_val)
            return {'download speed': d_speed_val, 'upload speed': u_speed_val}
        except:
            print("Test not yet finished")
        finally:
            time.sleep(2)
            self.driver.quit()
