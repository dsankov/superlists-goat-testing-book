from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

# Create your views here.
def home_page(request: HttpRequest) -> HttpResponse:
    """домашняя страница"""
    # if request.method == "POST":
    #     # print(request.POST)
    #     return HttpResponse(request.POST["item_text"])    
    return render(request, "home.html", {
        "new_item_text": request.POST.get("item_text", ""),
    })