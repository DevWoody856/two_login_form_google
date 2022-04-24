from allauth.account.views import LogoutView
from django.urls import path
from . import views

app_name = 'two_app'

urlpatterns = [
    path('login/', views.ShopSignUp.as_view(), name='shop-signup'),
    path('login-customer/', views.CustomerSignup.as_view(), name='customer-signUp'),
    path('shop/<str:username>/', views.shopProfile, name='shop-profile'),
    path('customer/<str:username>/', views.customerProfile, name='customer-profile'),
    path('account_logout/', LogoutView.as_view(), name='account_logout'),
]