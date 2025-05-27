import time
import warnings

from selenium.webdriver.support.wait import WebDriverWait

import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC


class TesteFuncionalidadeSistema(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)

    def test_search_google(self):
        driver = self.driver
        driver.get("https://www.google.com.br/")
        self.assertIn("Google", driver.title)
        elem = driver.find_element(by=By.NAME, value="q")
        elem.send_keys("selenium webdriver")
        elem = driver.find_element(by=By.NAME, value="btnI")
        # elem.click()
        driver.execute_script("arguments[0].click();", elem)
        # driver.implicitly_wait(5)  # seconds
        # elem = driver.find_element(by=By.XPATH, value="/html/body/div/div[1]/div/main/div/div[1]")
        elem = WebDriverWait(driver, timeout=5).until(
            lambda d: d.find_element(by=By.XPATH, value="/html/body/div/div[1]/div/main/div/div[1]"))
        self.assertEqual("WebDriver drives a browser natively; learn more about it.", elem.text)

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()