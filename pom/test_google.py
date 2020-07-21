import unittest
from selenium import webdriver
import google_page as goo
from selenium.webdriver.chrome.options import Options #opc chrome


class GoogleTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        options = Options() #opc chrome
        options.add_argument('--no-sandbox') #opc chrome
        cls.driver = webdriver.Chrome(chrome_options = options, executable_path = '../chromedriver')
     
    def test_search(self):
        google = goo.GooglePage(self.driver)
        google.open()
        google.search('Chocolates')

        self.assertEqual('Chocolates', google.keyword)
        
    @classmethod
    def tearDownClass(cls):
        cls.driver.close()

if __name__ == "__main__":
    unittest.main()

