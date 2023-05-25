from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from lists.models import Item, List

# Create your views here.
def home_page(request: HttpRequest) -> HttpResponse:
    """домашняя страница"""
    # if request.method == "POST":
    #     new_item_text = request.POST["item_text"]
    #     Item.objects.create(text=new_item_text)
    #     return redirect("/lists/the-only-list-in-the-world/")
    # items = Item.objects.all()
    return render(request, "home.html")
    
def view_list(request: HttpRequest) -> HttpResponse:
    items = Item.objects.all()
    return render(request, "list.html", {"items": items})

def new_list(request: HttpRequest) -> HttpResponse:
    """новый список"""
    list_ = List.objects.create()
    Item.objects.create(text=request.POST["item_text"], list=list_)
    return redirect("/lists/the-only-list-in-the-world/")
    