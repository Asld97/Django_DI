from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="crm-home"),
    path('products/', views.products, name="crm-product"),
    path('customer/', views.customer, name="crm-customer"),
    
]