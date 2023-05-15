from django.urls import resolve
from django.test import TestCase
from django.template.loader import render_to_string
from django.http import HttpRequest, HttpResponse

from lists.views import home_page

# Create your tests here.

        
class HomePageTest(TestCase):
    """Тест домашней страницы"""
    
       
    def test_home_page_returns_correct_html(self):
        response = self.client.get("/")
        self.assertTemplateUsed(response, "home.html")

    
        