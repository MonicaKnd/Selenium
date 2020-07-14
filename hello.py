import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pyunitreport import HTMLTestRunner



class Hello(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        options = Options()
        options.add_argument('--no-sandbox') # Bypass OS security model
        cls.driver = webdriver.Chrome(chrome_options = options, executable_path = r'C:/Program Files (x86)/Google/Chrome/Application/chromedriver.exe')
        driver = cls.driver
        driver.implicitly_wait(10)
    
    def test_hello(self):
        driver = self.driver
        driver.get('https://platzi.com')

    def test_visit_wikipedia(self):
        self.driver.get('https://www.wikipedia.org')

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main(verbosity = 2, testRunner = HTMLTestRunner(output = 'reportes', report_name = 'hello-report'))

