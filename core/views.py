from django.shortcuts import render
from menu.models import Menu
# Create your views here.
def home(request):
    menus = Menu.objects.all()
    return render(request, "core/home.html", {'menus':menus})

def about(request):
    return render(request, "core/about.html")