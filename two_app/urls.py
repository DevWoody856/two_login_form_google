from allauth.account.views import LogoutView
from django.urls import path
from . import views
from .views import HomeView

app_name = 'two_app'


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('accounts/login/', views.ShopLogin.as_view(), name='shop-signup'),
    # path('accounts/social/signup/', views.SocialSignUp.as_view(), name='social-signup'),
    path('accounts/login-customer/', views.CustomerLogin.as_view(), name='customer-signUp'),
    path('accounts/shop/<str:username>/', views.shopProfile, name='shop-profile'),
    path('accounts/customer/<str:username>/', views.customerProfile, name='customer-profile'),
    path('accounts/account_logout/', LogoutView.as_view(), name='account_logout'),
]