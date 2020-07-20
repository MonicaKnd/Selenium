import unittest
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By #Requieres esta libleria para las pausa explisitas
from selenium.webdriver.support.ui import WebDriverWait #Requieres esta libleria para las pausa explisitas
from selenium.webdriver.support import expected_conditions as EC #Requieres esta libleria para las pausa explisitas
from selenium.webdriver.chrome.options import Options #opc chrome

class AddRemoveElement(unittest.TestCase):

    def setUp(self):
        options = Options() #opc chrome
        options.add_argument('--no-sandbox') #opc chrome
        self.driver = webdriver.Chrome(chrome_options = options, executable_path = './chromedriver')
        driver = self.driver
        driver.get("http://the-internet.herokuapp.com/")
        driver.find_element_by_link_text('Add/Remove Elements').click()

    def test_add_remove(self):
        driver = self.driver

        elements_added = int(input('How many elements will you add?: '))
        elements_removed = int(input('How many elements will you remove?: '))
        total_elements = elements_added - elements_removed

        add_button = driver.find_element_by_xpath('//*[@id="content"]/div/button')
        sleep(3)

        for i in range(elements_added):
            add_button.click()

        for i in range(elements_removed):
            try:
                delete_button = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.LINK_TEXT, 'Delete'))) #Pausas explisitas
                #delete_button = driver.find_element_by_class_name('added-manually')
                delete_button.click()
            except:
                print("You're trying to delete more elements the existent")
                break

        if total_elements > 0:
            print("There are {total_elements} elements on screen")
        else:
            print("There 0 are elements on screen")
        sleep(3)

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main(verbosity = 2)

