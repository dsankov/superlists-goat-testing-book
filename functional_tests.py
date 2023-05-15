from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pretty_errors
import unittest
import time

class NewVisitorTest(unittest.TestCase):
    """тест нового посетителя"""
    
    def setUp(self) -> None:
        # return super().setUp()
        self.browser = webdriver.Firefox()
        
    def tearDown(self) -> None:
        # return super().tearDown()
        self.browser.quit()
        
    def test_can_start_a_list_and_retrieve_it_later(self):
        """тест: можно начать список и получить его позже"""
        # Эдит слышала про крутое новое онлайн-приложение со
        # списком неотложных дел. Она решает оценить его
        # домашнюю страницу
        self.browser.get('http://localhost:8000')

        # Она видит, что заголовок и шапка страницы говорят о
        # списках неотложных дел
        self.assertIn('To-Do', self.browser.title) 
  
        header_text = self.browser.find_element(by=By.TAG_NAME, value="h1").text
        self.assertIn("To-Do", header_text)

        # Ей сразу же предлагается ввести элемент списка
        inputbox     = self.browser.find_element(By.ID, "id_new_item")
        self.assertEqual(
            inputbox.get_attribute("placeholder"),
            "Enter a to-do item"    
        )
        
        # Она набирает в текстовом поле "Купить павлиньи перья" (ее хобби –
        # вязание рыболовных мушек)
        inputbox.send_keys("Купить павлинья перья")
        
        # Когда она нажимает enter, страница обновляется, и теперь страница
        # содержит "1: Купить павлиньи перья" в качестве элемента списка
        inputbox.send_keys(Keys.ENTER)
        time.sleep(3)
        
        table = self.browser.find_element(By.ID, "id_list_table")
        rows = table.find_elements(By.TAG_NAME, "tr")

        self.assertTrue(
            any(row.text == "1: Купить павлинья перья" for row in rows),
            "Новый элемент списка не появился в таблице"
        )
        
        # Текстовое поле по-прежнему приглашает ее добавить еще один элемент.
        # Она вводит "Сделать мушку из павлиньих перьев"
        # (Эдит очень методична)
        # Страница снова обновляется, и теперь показывает оба элемента ее списка
        # Эдит интересно, запомнит ли сайт ее список. Далее она видит, что
        # сайт сгенерировал для нее уникальный URL-адрес – об этом
        # выводится небольшой текст с объяснениями.
        # Она посещает этот URL-адрес – ее список по-прежнему там.
        # Удовлетворенная, она снова ложится спать
        
        self.fail('Закончить тест!') 
    
if __name__ == "__main__":
    unittest.main()
