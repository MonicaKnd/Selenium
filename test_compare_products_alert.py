import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options #opc chrome

class CompareProducts(unittest.TestCase):

    def setUp(self):
        options = Options() #opc chrome
        options.add_argument('--no-sandbox') #opc chrome
        self.driver = webdriver.Chrome(chrome_options = options, executable_path = './chromedriver')
        driver = self.driver
        driver.implicitly_wait(30)
        driver.maximize_window()
        driver.get("http://automationpractice.com/index.php")

    def test_compare_products_alert(self):
        driver = self.driver
        search_field = driver.find_element_by_name('search_query')
        search_field.clear()

        search_field.send_keys('Blouse')
        search_field.submit()

        driver.find_element_by_class_name('add_to_compare').click()
        driver.find_element_by_xpath('/html/body/div/div[2]/div/div[3]/div[2]/div[1]/div[2]/form/button').click()
        driver.find_element_by_xpath('/html/body/div/div[2]/div/div[3]/div/div/table/tbody/tr[1]/td[2]/div[5]/div/div/a[1]/span').click()

        #alert = driver.switch_to_alert()
        #alert_text = alert.txt    #Esto es para revisar el texto del alerta

        #self.assertEqual('Aqui va el texto del alerta', alert_text)

        #alert.accept()

        #Esta prueba es para alertas pero esta pagina no lo tiene

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main(verbosity = 2)

