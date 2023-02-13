from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

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
    path('user/', views.userPage, name="crm-user-page" ),
    path('account/', views.accountSettings, name="crm-account"),

    path('reset_password/', auth_views.PasswordResetView.as_view(template_name="accounts/password_reset.html"), name="reset_password"),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name="accounts/password_reset_sent.html"), name="password_reset_done"),
    path('reset_password_confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="accounts/password_reset_form.html"), name="password_reset_confirm"), # uidb64 - coding method for password
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name="accounts/password_reset_done.html"), name="password_reset_complete"),
]