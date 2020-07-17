import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options #opc chrome

class MonthOptions(unittest.TestCase):

    def setUp(self):
        options = Options() #opc chrome
        options.add_argument('--no-sandbox') #opc chrome
        self.driver = webdriver.Chrome(chrome_options = options, executable_path = './chromedriver')
        driver = self.driver
        driver.implicitly_wait(30)
        driver.maximize_window()
        driver.get("https://www.facebook.com/")

    #metodo para el select
    def test_select_month(self):
        exp_options = ['Mes', 'ene', 'feb', 'mar', 'abr', 'may', 'jun', 'jul', 'ago', 'sep', 'oct', 'nov', 'dic']
        act_options =[]

        select_month = Select(self.driver.find_element_by_id('month'))
        
        self.assertEqual(13, len(select_month.options)) #validar que tenga 13 opciones

        for option in select_month.options:
            act_options.append(option.text)

        self.assertEqual('Jul', select_month.first_selected_option.text) #Esta opción cambia dependiendo del mes en el que se este cursando

        select_month.select_by_visible_text('Feb')

        #self.assertTrue('lo que aparece en la URL' in self.driver.current_url)

        select_month = Select(self.driver.find_element_by_id('month'))
        select_month.select_by_index(0)

    def tearDown(self):
        self.driver.implicitly_wait(3)
        self.driver.close()

if __name__ == "__main__":
    unittest.main(verbosity = 2)

