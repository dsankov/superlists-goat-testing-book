from django.urls import resolve
from django.test import TestCase
from django.template.loader import render_to_string
from django.http import HttpRequest, HttpResponse

from lists.views import home_page

# Create your tests here.

        
class HomePageTest(TestCase):
    """Тест домашней страницы"""
    
    def test_root_url_resolves_to_home_page_view(self):
        """
        тест: корневой урл преобразуется в представление домашней страницы
        """
        
        found = resolve("/")
        self.assertEqual(found.func, home_page)
        
    def test_home_page_returns_correct_html(self):
        """тест: домашняя страница возвращает правильный код
        """
        
        request = HttpRequest()
        response = home_page(request)
        
        response = self.client.get("/")
        html = response.content.decode("utf8")
        
        self.assertTrue(html.startswith("<html>"), msg=html)
        self.assertIn("<title>To-Do lists</title>", html)
        self.assertTrue(html.strip().endswith("</html>"))
        
        expected_html = render_to_string("home.html")
        self.assertIn(html, expected_html)
        
        self.assertTemplateUsed(response, "home.html")
        self.assertTemplateUsed(response, "wrng.html")
    
        