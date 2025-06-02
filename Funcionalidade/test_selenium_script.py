import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import selenium.common.exceptions

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

# Feito por Pedro Mendes Lima
    def test_02_navegacao_menu_admin(self):
        try:
            self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
            username_input = self.wait.until(EC.presence_of_element_located((By.NAME, "username")))
            username_input.send_keys("Admin")

            password_input = self.driver.find_element(By.NAME, "password")
            password_input.send_keys("admin123")

            login_button = self.driver.find_element(By.CSS_SELECTOR, "[type='submit']")
            login_button.click()

            self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".oxd-topbar-header-breadcrumb h6")))

            admin_menu = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Admin']")))
            admin_menu.click()

            admin_header = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".oxd-topbar-header-breadcrumb h6")))

            self.assertIn("Admin", admin_header.text,"Texto 'Admin' não encontrado no cabeçalho")
            self.assertIn("admin", self.driver.current_url.lower(),"URL não contém 'admin'")

            users_table = self.wait.until( EC.presence_of_element_located((By.CSS_SELECTOR, ".oxd-table")))
            self.assertTrue(users_table.is_displayed(),"Tabela de usuários não está visível")

            table_rows = self.driver.find_elements(By.CSS_SELECTOR, ".oxd-table-body .oxd-table-row")
            self.assertGreater(len(table_rows), 0,"Nenhum usuário encontrado na tabela")

            add_button = self.driver.find_element(By.CSS_SELECTOR, ".oxd-button--secondary")
            self.assertTrue(add_button.is_displayed(),"Botão 'Add' não está visível")

            search_section = self.driver.find_element(By.CSS_SELECTOR, ".oxd-form")
            self.assertTrue(search_section.is_displayed(),"Seção de busca não está visível")

            print("✅ Teste de navegação no menu Admin passou!")

        except Exception as e:
            self.fail(f"Erro inesperado durante o teste de navegação: {str(e)}")

    def tearDown(self):
        if self.driver:
            self.driver.quit()

class TestSuiteOrangeHRM:
    @staticmethod
    def rodar_testes():
        suite = unittest.TestSuite()
        suite.addTest(TestOrangeHRM('test_01_login_valido'))
        suite.addTest(TestOrangeHRM('test_02_navegacao_menu_admin'))

        runner = unittest.TextTestRunner(verbosity=2)
        result = runner.run(suite)
        return result


if __name__ == "__main__":
    unittest.main(verbosity=2, exit=False)
    TestSuiteOrangeHRM.rodar_testes()