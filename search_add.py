import unittest
from ddt import ddt, data, unpack
from selenium import webdriver
from selenium.webdriver.chrome.options import Options #opc chrome

@ddt
class SearchDDT(unittest.TestCase):
    def setUp(self):
        options = Options() #opc chrome
        options.add_argument('--no-sandbox') #opc chrome
        self.driver = webdriver.Chrome(chrome_options = options, executable_path = './chromedriver')
        driver = self.driver
        driver.implicitly_wait(15)
        driver.maximize_window()
        driver.get("https://www.sumitel.com/")

    @data(('PCM', 7), ('WINDOWS', 1))
    @unpack

    def test_search_ddt(self, search_value, expected_count):
        driver = self.driver

        close = driver.find_element_by_xpath('/html/body/div[1]/main/div[1]/div[12]/div/div/div/div[2]/a')
        close.click()

        search_field = driver.find_element_by_name('producto')
        search_field.clear()
        search_field.send_keys(search_value)
        search_field.submit()

       
        products = driver.find_elements_by_xpath('//strong[@class="product-item-name"]/a')
        print(f'Found {len(products)} products')

        for product in products:
            print(product.text)

        self.assertEqual(expected_count, len(products))
    
    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()

