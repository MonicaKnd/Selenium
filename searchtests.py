import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options #opc chrome

class HomePageTest(unittest.TestCase):

    def setUp(self):
        options = Options() #opc chrome
        options.add_argument('--no-sandbox') #opc chrome
        self.driver = webdriver.Chrome(chrome_options = options, executable_path = './chromedriver')
        driver = self.driver
        driver.get("http://automationpractice.com/index.php")
        driver.maximize_window()
        driver.implicitly_wait(15)
    
    #busquedas de forma automatizada
    def test_search_tee(self):
        driver = self.driver
        search_field = driver.find_element_by_name("search_query")
        search_field.clear()

        search_field.send_keys('Drees') # simulación del teclado
        search_field.submit()

    def test_search_blouse(self):
        driver = self.driver
        search_field = driver.find_element_by_name('search_query')

        search_field.send_keys('Blouse')
        search_field.submit()

        products = driver.find_elements_by_xpath('//*[@id="center_column"]/ul/li/div/div[1]/div/a[2]')
        self.assertEqual(1, len(products))

    # fin de busqueda
    
    def test_search_text_field(self):
        search_field = self.driver.find_element_by_id("search_query_top")

    def test_search_text_field_by_name(self):
        search_field = self.driver.find_element_by_name("search_query")

    def test_search_text_field_class_name(self):
        search_field = self.driver.find_element_by_class_name("search_query")    

    def test_search_button_enabled(self):    
        button = self.driver.find_element_by_class_name("btn-default")

    def test_count_of_articulos_imagenes(self):
        card_list = self.driver.find_element_by_class_name("product_list")
        cards = card_list.find_elements_by_tag_name('img')
        self.assertEqual(7, len(cards)) # validacion de que efectivamente sean 7 imagenes

    def test_xpath(self):
        promo = self.driver.find_element_by_xpath('//*[@id="htmlcontent_home"]/ul/li[2]/a/img')

    def test_shopping_cart(self):
        shopping_cart_icon = self.driver.find_element_by_css_selector("div.shopping_cart")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main(verbosity = 2)