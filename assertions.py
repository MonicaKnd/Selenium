import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options #opc chrome
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

class HomePageTest(unittest.TestCase):

    def setUp(self):
        options = Options() #opc chrome
        options.add_argument('--no-sandbox') #opc chrome
        self.driver = webdriver.Chrome(chrome_options = options, executable_path = './chromedriver')
        driver = self.driver
        driver.implicitly_wait(15)
        driver.maximize_window()
        driver.get("http://automationpractice.com/index.php")

    #metodos para los assertions
    def test_search_field(self):
        self.assertTrue(self.is_element_present(By.NAME, 'search_query'))

    def test_language_option(self):
        self.assertTrue(self.is_element_present(By.ID, 'aqui_va_elnom_del_ID'))

    def tearDown(self):
        self.driver.quit()

    def is_element_present(self, how, what): #Función para identificar cuando un elemento esta presente de acuerdo a sus parametros
        try: 
            self.driver.find_element(by = how, value= what)
        except NoSuchElementException as variable:
            return False
        return True


if __name__ == "__main__":
    unittest.main(verbosity = 2)

#ghKU