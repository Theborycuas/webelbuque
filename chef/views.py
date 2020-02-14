from django.shortcuts import render
from .models import Chef
# Create your views here.
def chef(request):
    chefs = Chef.objects.all()
    return render(request, "chef/chef.html", {'chefs':chefs})