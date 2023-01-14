from django.shortcuts import render
from menuapp.models import Menu


def index(request):
    menu_list = Menu.objects.all()
    context = {
        'menu_list': menu_list
    }
    return render(request, 'menuapp/index.html', context)


def menu(request):
    menu_list = Menu.objects.all()
    context = {
        'menu_list': menu_list
    }

    return render(request, "menuapp/menu.html", context)
