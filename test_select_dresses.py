import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options #opc chrome

class DressesOptions(unittest.TestCase):

    def setUp(self):
        options = Options() #opc chrome
        options.add_argument('--no-sandbox') #opc chrome
        self.driver = webdriver.Chrome(chrome_options = options, executable_path = './chromedriver')
        driver = self.driver
        driver.implicitly_wait(30)
        driver.maximize_window()
        driver.get("http://automationpractice.com/index.php")

    #metodo para el select
    def test_select_dresses(self):
        exp_options = ['Price: Lowest first', 'Price: Highest first', 'Product Name: A to Z', 'Product Name: Z to A', 'In stock', 'Reference: Lowest first', 'Reference: Highest first']
        act_options =[]

        select_dresses = Select(self.driver.find_element_by_id('selectProductSort'))
        
        self.assertEqual(7, len(select_dresses.options)) #validar que tenga 7 opciones

        for option in select_dresses.options:
            act_options.append(option.text)

        self.assertEqual('--', select_dresses.first_selected_option.text)

        select_dresses.select_by_visible_text('Price: Lowest first')

        #self.assertTrue('lo que aparece en la URL' in self.driver.current_url)

        select_dresses = Select(self.driver.find_element_by_id('selectProductSort'))
        select_dresses.select_by_index(0)

    def tearDown(self):
        self.driver.implicitly_wait(3)
        self.driver.close()

if __name__ == "__main__":
    unittest.main(verbosity = 2)

