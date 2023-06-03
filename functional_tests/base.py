import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import WebDriverException
from django.contrib.staticfiles.testing import StaticLiveServerTestCase


MAX_WAIT = 3

class FunctionalTest(StaticLiveServerTestCase):
    """функциональный тест"""
    
    def setUp(self) -> None:
        """Установка"""
        # return super().setUp()
        self.browser = webdriver.Firefox()
        staging_server = os.environ.get("STAGING_SERVER")
        if staging_server:
            self.live_server_url = "http://" + staging_server
        
    def tearDown(self) -> None:
        """демонтаж"""
        # return super().tearDown()
        self.browser.quit()
        
    def wait_for_row_in_list_table(self, row_text):
        """подтверждение строки в таблице списка"""
        start_time = time.time()
        while True:
            try:
                table = self.browser.find_element(By.ID, "id_list_table")
                rows = table.find_elements(By.TAG_NAME, "tr")
                rows_text = [row.text for row in rows]
                # logger.debug(f"looking for {row_text} in {rows_text}")
                self.assertIn(row_text, rows_text)
                return
            except (AssertionError, WebDriverException) as e:
                if time.time() - start_time > MAX_WAIT:
                    # logger.critical(f"not found {row_text} in {[row.text for row in rows]}")                    
                    raise e
                time.sleep(0.5)
