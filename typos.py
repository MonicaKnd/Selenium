import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options #opc chrome

class Typos(unittest.TestCase):

    def setUp(self):
        options = Options() #opc chrome
        options.add_argument('--no-sandbox') #opc chrome
        self.driver = webdriver.Chrome(chrome_options = options, executable_path = './chromedriver')
        driver = self.driver      
        driver.get("http://the-internet.herokuapp.com/")
        driver.find_element_by_link_text("Typos").click()


    def test_find_typo(self):
        driver = self.driver

        paragraph_to_check = driver.find_element_by_css_selector("#content > div > p:nth-child(2)")
        text_to_check = paragraph_to_check.text
        print(text_to_check)

        tries = 1
        found = False
        correct_text = "Sometimes you'll see a typo, other times you won,t."

        while text_to_check != correct_text:
            paragraph_to_check = driver.find_element_by_css_selector("#content > div > p:nth-child(3)")
            text_to_check = paragraph_to_check.text
            driver.refresh()
            tries += 1

        while not found:
            if text_to_check == correct_text:
                tries == 1
                driver.refresh()
                found = True

        self.assertEqual(found, True)

        print("It took {} tries to find the typo".format(tries))

    def tearDown(self):
        self.driver.close() 


if __name__ == "__main__":
    unittest.main(verbosity = 2)

