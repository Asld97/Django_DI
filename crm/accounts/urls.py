from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="crm-home"),
    path('products/', views.products, name="crm-product"),
    path('customer/<str:pk>', views.customer, name="crm-customer"),

    path('create_order/<str:pk>', views.createOrder, name="crm-create-order"),
    path('update_order/<str:pk>', views.updateOrder, name="crm-update-order"),
    path('delete_order/<str:pk>', views.deleteOrder, name="crm-delete-order"),

    path('register/', views.registerPage, name="crm-register"),
    path('login/', views.loginPage, name="crm-login"),
    path('logout/', views.logoutUser, name="crm-logout"),
    path('user/', views.userPage, name="crm-user-page" )
]