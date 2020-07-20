import unittest
from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.options import Options #opc chrome

class Tables(unittest.TestCase):

    def setUp(self):
        options = Options() #opc chrome
        options.add_argument('--no-sandbox') #opc chrome
        self.driver = webdriver.Chrome(chrome_options = options, executable_path = './chromedriver')
        driver = self.driver      
        driver.get("http://the-internet.herokuapp.com/")
        driver.find_element_by_link_text("Sortable Data Tables").click()


    def test_sort_tables(self):
        driver = self.driver

        table_data = [[] for i in range(5)]
        print(table_data)

        for i in range(5):
            header = driver.find_element_by_xpath('//*[@id="table1"]/thead/tr/th[{}]/span'.format(i + 1))
            table_data[i].append(header.text)

            for j in range(4):
                row_data = driver.find_element_by_xpath(f'//*[@id="table1"]/tbody/tr[{j + 1}]/td[{i + 1}]')
                table_data[i].append(row_data.text)

        print(table_data)

    def tearDown(self):
        self.driver.close() 


if __name__ == "__main__":
    unittest.main()

