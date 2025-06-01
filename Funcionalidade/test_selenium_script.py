import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

class TestOrangeHRM(unittest.TestCase):
    def setUp(self):
        chrome_options = Options()
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--window-size=1920,1080")

        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.implicitly_wait(10)
        self.wait = WebDriverWait(self.driver, 15)

# Feito Por Pedro Siqueira
    def test_01_login_valido(self):
        try:
            self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
            username_input = self.wait.until(EC.presence_of_element_located((By.NAME, "username")))
            username_input.send_keys("Admin")
            password_input = self.driver.find_element(By.NAME, "password")
            password_input.send_keys("admin123")
            login_button = self.driver.find_element(By.CSS_SELECTOR, "[type='submit']")
            login_button.click()
            dashboard_element = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".oxd-topbar-header-breadcrumb h6")))
            self.assertIn("Dashboard", dashboard_element.text,"Elemento não Encontrado")
            self.assertIn("dashboard", self.driver.current_url.lower(),"URL não contém 'dashboard'")
            print("✅ Teste de login válido passou!")
        except Exception as e:
            self.fail(f"Erro no login: {str(e)}")

    def tearDown(self):
        if self.driver:
            self.driver.quit()

class TestSuiteOrangeHRM:
    def rodar_testes(self):
        suite = unittest.TestSuite()
        suite.addTest(TestOrangeHRM('test_01_login_valido'))

        runner = unittest.TextTestRunner(verbosity=2)
        result = runner.run(suite)
        return result


if __name__ == "__main__":
    unittest.main(verbosity=2, exit=False)
    TestSuiteOrangeHRM.rodar_testes()