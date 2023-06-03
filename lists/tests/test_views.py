from django.urls import resolve
from django.test import TestCase
from django.template.loader import render_to_string
from django.http import HttpRequest, HttpResponse

from lists.views import home_page
from lists.models import Item, List


# Create your tests here.
class HomePageTest(TestCase):
    """Тест домашней страницы"""
       
    def test_home_page_returns_correct_html(self):
        """тест: используется домашний шаблон"""
        response = self.client.get("/")
        self.assertTemplateUsed(response, "home.html")    
                
class ListViewTest(TestCase):
    """тест представления списка"""
    
    def test_uses_list_template(self):
        """тест: используется шаблон списка"""
        list_ = List.objects.create()
        response = self.client.get(f"/lists/{list_.id}/")
        self.assertTemplateUsed(response, "list.html")
    
    def test_displays_only_items_for_that_list(self):
        """тест: отображаются элементы только для нужного списка"""
        correct_list = List.objects.create()
        Item.objects.create(text="itemey 1", list=correct_list)
        Item.objects.create(text="itemey 2", list=correct_list)
        other_list = List.objects.create()
        Item.objects.create(text="list 2 itemey 1", list=other_list)
        Item.objects.create(text="list 2 itemey 2", list=other_list)
        
        response = self.client.get(f"/lists/{correct_list.id}/")
        
        self.assertContains(response, "itemey 1")
        self.assertContains(response, "itemey 2")
        self.assertNotContains(response, "list 2 itemey 1")
        self.assertNotContains(response, "list 2 itemey 2")
        
    def test_passes_correct_link_to_template(self):
       """тест: передается правильный шаблон списка"""
       other_list = List.objects.create()
       correct_list = List.objects.create()
       response = self.client.get(f"/lists/{correct_list.id}/")
       self.assertEqual(response.context["list"], correct_list)
        
        
class NewListTest(TestCase):
    """тест нового списка"""
        
    def test_can_save_a_POST_request(self):
        """тест: можно сохранить post-запрос"""
        self.client.post(
            path="/lists/new", 
            data={"item_text": "A new list item"}
            )
        self.assertEqual(Item.objects.count(), 1)
        new_item = Item.objects.first()
        self.assertEqual(new_item.text, "A new list item")
        
    def test_redirects_after_POST(self):
        """тест: переадресует после post-запроса"""
        response = self.client.post(
            path="/lists/new", 
            data={"item_text": "A new list item"},
            )
        new_list = List.objects.first()
        self.assertRedirects(response, f"/lists/{new_list.id}/")
        # self.assertEqual(response.status_code, 302)
        # self.assertEqual(response["location"], "/lists/the-only-list-in-the-world/")
    
class NewItemTest(TestCase):
    """Тест нового списка"""
    
    def test_can_save_a_POST_request_to_an_existing_list(self):
        """тест: можно сохранить post-запрос в существующий срисок"""
        other_list = List.objects.create()
        correct_list = List.objects.create()
        
        self.client.post(
            path=f"/lists/{correct_list.id}/add_item",
            data={
                "item_text": "A new item for an existing list"
            },
        )
        
        self.assertEqual(Item.objects.count(), 1)
        new_item = Item.objects.first()
        self.assertEqual(new_item.text, "A new item for an existing list")
        self.assertEqual(new_item.list, correct_list)
        
    def test_redirects_lo_list_view(self):
        """тест: переадрессует в представление списка"""
        other_list = List.objects.create()
        correct_list = List.objects.create()
        
        response = self.client.post(
            path=f"/lists/{correct_list.id}/add_item",
            data={
                "item_text": "A new item for an existing list"
            },
        )
        
        self.assertRedirects(response, f"/lists/{correct_list.id}/")