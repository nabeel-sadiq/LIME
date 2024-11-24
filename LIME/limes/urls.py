from django.urls import path
from . import views

urlpatterns = [
    path('', views.limes, name="limes"),
    path('create/', views.lime_create, name="lime_create"),
]