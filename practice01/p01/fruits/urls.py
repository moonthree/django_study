from django.urls import path
from . import views

urlpatterns = [
    path('fruit/', views.fruit, name='fruit'),
]
