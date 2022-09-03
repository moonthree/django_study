from django.urls import path
from . import views

app_name="menus"
urlpatterns = [
    path('food/', views.food, name='food'),
    path('receipt/', views.receipt, name='receipt'),
    path('drink/', views.drink, name='drink'),
]
