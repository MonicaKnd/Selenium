import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options #opc chrome

class RegisterNewUser(unittest.TestCase):

    def setUp(self):
        options = Options() #opc chrome
        options.add_argument('--no-sandbox') #opc chrome
        self.driver = webdriver.Chrome(chrome_options = options, executable_path = './chromedriver')
        driver = self.driver
        driver.implicitly_wait(30)
        driver.maximize_window()
        driver.get("http://automationpractice.com/index.php")

    #metodos para los assertions
    def test_new_user(self):
        driver = self.driver
        driver.find_element_by_xpath('/html/body/div/div[1]/header/div[2]/div/div/nav/div[1]/a').click()
        driver.find_element_by_link_text('Sign in').click()

        create_account_button = driver.find_element_by_xpath('//*[@id="SubmitCreate"]/span')
        self.assertTrue(create_account_button.is_displayed() and create_account_button.is_enabled())
        create_account_button.click()

        self.assertEqual('Login - My Store', driver.title)
        #aqui van los campos del formulario a llenar
        email_address = driver.find_element_by_id('email_create')
        submit_button = driver.find_element_by_xpath('//*[@id="SubmitCreate"]')
        #verifica si estan habilitados los campos
        self.assertTrue(email_address.is_enabled()
        and submit_button.is_enabled())
        #llena los campos
        email_address.send_keys('test3@gmail.com')
        driver.implicitly_wait(5)
        submit_button.click()

    def tearDown(self):
        self.driver.implicitly_wait(3)
        self.driver.close()


if __name__ == "__main__":
    unittest.main(verbosity = 2)

