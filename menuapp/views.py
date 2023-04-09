from django.http import HttpResponse
from django.shortcuts import render
from .models import MenuItem

def menu_list(request, menu_id):
    Menu = MenuItem.objects.get(url = menu_id)
    context = {
        'Menu' : Menu,
    }
    return render(request, 'menu_list.html', context)

def home(request):
    return render(request, 'home.html')
