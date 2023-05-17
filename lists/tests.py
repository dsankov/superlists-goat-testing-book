from django.urls import resolve
from django.test import TestCase
from django.template.loader import render_to_string
from django.http import HttpRequest, HttpResponse

from lists.views import home_page

# Create your tests here.

        
class HomePageTest(TestCase):
    """Тест домашней страницы"""
    
       
    def test_home_page_returns_correct_html(self):
        """тест: используется домашний шаблон"""
        response = self.client.get("/")
        self.assertTemplateUsed(response, "home.html")

    def test_can_save_a_POST_request(self):
        """тест: можно сохранить post-запрос"""
        response = self.client.post("/", data={"item_text": "A new list item"})
        # print(response.content)
        # print("__________")
        # print(response.content.decode())
        # print("qqq")
        self.assertIn(
            "A new list item",
            response.content.decode()
        )
        self.assertTemplateUsed(response, "home.html")
        