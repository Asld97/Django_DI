from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="crm-home"),
    path('products/', views.products, name="crm-product"),
    path('customer/<str:pk>', views.customer, name="crm-customer"),
    
]