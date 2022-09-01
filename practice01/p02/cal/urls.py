from django.urls import path
from . import views

app_name = "cal"
urlpatterns = [
    path('calc/', views.calc, name='calc'),
    path('result/', views.result, name='result'),
]
