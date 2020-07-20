import unittest
from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.options import Options #opc chrome

class DynamicElements(unittest.TestCase):

    def setUp(self):
        options = Options() #opc chrome
        options.add_argument('--no-sandbox') #opc chrome
        self.driver = webdriver.Chrome(chrome_options = options, executable_path = './chromedriver')
        driver = self.driver      
        driver.get("http://the-internet.herokuapp.com/")
        driver.find_element_by_link_text('Disappearing Elements').click()

    def test_name_elements(self):
        driver = self.driver

        options = []
        menu = 5
        tries = 1
        
        while len(options) < 5:
            options.clear()

            for i in range(menu):
                try:
                    option_name = driver.find_element_by_xpath('/html/body/div[2]/div/div/ul/li[{}]/a'.format(i+1))
                    options.append(option_name.text)
                    print(options)
                except:
                    print('Option number {} is NOT FOUND'.format(i + 1))
                    tries += 1
                    driver.refresh()

        print('Finished in {} tries'.format(tries))
 
    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main(verbosity = 2)

