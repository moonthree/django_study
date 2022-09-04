from django.urls import path
from . import views
app_name="fruits"
urlpatterns = [
    #1 
    path('fruit/', views.fruit, name='fruit'),
    #2-1
    path('price/<str:thing>/<int:cnt>/', views.price, name='price'),
    #2-2
    path('cal/<int:a>/<int:b>/', views.cal, name='cal'),
    #2-3
    path('first/', views.first, name='first'),
    path('second/', views.second, name='second'),
]
