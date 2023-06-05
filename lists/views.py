# from log2d import Log
from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from django.core.exceptions import ValidationError
from lists.models import Item, List

# logger = Log("views\t").logger
# Create your views here.
def home_page(request: HttpRequest) -> HttpResponse:
    """домашняя страница"""

    return render(request, "home.html")
    
def view_list(request: HttpRequest, list_id) -> HttpResponse:
    """представление списка"""

    # logger.debug(f"view list: {list_id=}")
    list_ = List.objects.get(id=list_id)
    error = None
    if request.method == "POST":
        try:
            item = Item.objects.create(
                text=request.POST["item_text"],
                list=list_
            )
            item.full_clean()
            # print("!!!!!!!!!!!")
            item.save()
            return redirect(f"/lists/{list_.id}/")
        except ValidationError:
            item.delete()
            error = "You cant have an empty list item"
            
    return render(
        request=request, 
        template_name="list.html", 
        context={
            "list": list_,
            "error": error,
            }
        )

def new_list(request: HttpRequest) -> HttpResponse:
    """новый список"""
   
    list_ = List.objects.create()
    # logger.debug(f"create new item in list {list_.id}")
    item = Item.objects.create(text=request.POST["item_text"], list=list_)
    try:
        item.full_clean()
        item.save()
    except ValidationError:
        list_.delete()
        item.delete()
        error = "You cant have an empty list item"
        return render(request=request, template_name="home.html", 
                      context={"error": error}        
                    )
    return redirect(f"/lists/{list_.id}/")
    
