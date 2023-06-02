# from log2d import Log
from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from lists.models import Item, List

# logger = Log("views\t").logger
# Create your views here.
def home_page(request: HttpRequest) -> HttpResponse:
    """домашняя страница"""
    # if request.method == "POST":
    #     new_item_text = request.POST["item_text"]
    #     Item.objects.create(text=new_item_text)
    #     return redirect("/lists/the-only-list-in-the-world/")
    # items = Item.objects.all()
    return render(request, "home.html")
    
def view_list(request: HttpRequest, list_id) -> HttpResponse:
    """представление списка"""

    # logger.debug(f"view list: {list_id=}")
    list_ = List.objects.get(id=list_id)
    items = Item.objects.filter(list=list_)
    return render(request, "list.html", {"list": list_})

def new_list(request: HttpRequest) -> HttpResponse:
    """новый список"""
   
    list_ = List.objects.create()
    # logger.debug(f"create new item in list {list_.id}")
    Item.objects.create(text=request.POST["item_text"], list=list_)
    return redirect(f"/lists/{list_.id}/")
    
def add_item(request: HttpRequest, list_id) -> HttpResponse:
    """добавить элемент в список"""
    list_ = List.objects.get(id=list_id)
    # logger.debug(f"add item to list {list_.id}")
    Item.objects.create(
        text=request.POST["item_text"],
        list=list_
    )
    return redirect(f"/lists/{list_.id}/")
