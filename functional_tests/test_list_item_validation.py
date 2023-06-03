
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from unittest import skip

from .base import FunctionalTest

# from log2d import Log
# logger = Log("functional_test\t").logger

class ItemValidationTest(FunctionalTest):
    """тест валидации элементов списка"""        
    
    # @skip
    def test_cannot_add_empty_list_items(self):
        """тест: нельзя добавлять пустые элементы списка"""
        # Эдит открывает домашнюю страницу и случайно пытается отправить
        # пустой элемент списка. Она нажимает Enter на пустом поле ввода
        
        # Домашняя страница обновляется, и появляется сообщение об ошибке,
        # которое говорит, что элементы списка не должны быть пустыми
        
        # Она пробует снова, теперь с неким текстом для элемента, и теперь
        # это срабатывает
        
        # Как ни странно, Эдит решает отправить второй пустой элемент списка
        
        # Она получает аналогичное предупреждение на странице списка
        # И она может его исправить, заполнив поле неким текстом
        self.fail('напиши меня!')