from django.urls import path
from menuapp import views as menuapp

app_name = 'menuapp'

urlpatterns = [
    path('menu/', menuapp.menu, name='menu'),
]
