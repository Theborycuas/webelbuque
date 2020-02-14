from django.shortcuts import render
from menu.models import Menu
from blog.models import Post
# Create your views here.
def home(request):
    menus = Menu.objects.all()
    posts = Post.objects.all()
    return render(request, "core/home.html", {'menus':menus, 'posts':posts})

def about(request):
    return render(request, "core/about.html")