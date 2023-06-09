from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from .base import FunctionalTest
# from log2d import Log

# logger = Log("functional_test\t").logger

        
class LayoutAndStylingTest(FunctionalTest):
    """тест макета и стилевого оформления"""
            
    def test_layout_and_styling(self):
        """тест макета стилевого оформления"""
        # Эдит открывает домашнюю страницу
        self.browser.get(self.live_server_url)
        self.browser.set_window_size(1024, 768)
        
        # Она замечает поле ввода по центру
        inputbox = self.browser.find_element(By.ID, "id_new_item")
        # time.sleep(5)
        self.assertAlmostEqual(
            inputbox.location["x"] + inputbox.size["width"] / 2,
            512,
            delta=10
        )
        
        # Она начинает новый список и видит, что поле ввода - по центру
        inputbox.send_keys("testing")
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table("1: testing")
        inputbox = self.browser.find_element(By.ID, "id_new_item")
        self.assertAlmostEqual(
            inputbox.location["x"] + inputbox.size["width"] / 2,
            512,
            delta=10
        )
        