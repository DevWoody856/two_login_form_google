from allauth.account.views import LoginView, LogoutView
from allauth.socialaccount.views import SignupView
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views.generic import TemplateView

from two_app.decorators import shop_required, customer_required
from two_app.models import CustomUser, Shop, Customer


class HomeView(LoginView):
    template_name = "two_app/index.html"


class ShopLogin(LoginView):
    template_name = 'two_app/shop-login.html'


class CustomerLogin(LoginView):
    template_name = 'two_app/customer-login.html'



@login_required(redirect_field_name=None)
def shopProfile(request, username):

    # This is Auth guard.
    if not request.user.username == username or Customer.objects.filter(user__email=request.user.email).exists():
        return redirect('two_app:customer-profile', request.user.username)

    user = CustomUser.objects.get(username=username)

    if Shop.objects.filter(user__username=request.user.username).exists():
        text = Shop.objects.filter(user__username=username).values_list('description', flat=True).get()
    else:
        # Create new shop user here
        text = Shop.objects.create(user=user, description="First Comment")
        text = text.description
    context = {
        'user': user,
        'text': text
    }
    template = "two_app/shop-profile.html"
    return render(request, template, context)



@login_required(redirect_field_name=None)
def customerProfile(request, username):

    # This is Auth guard.
    if not request.user.username == username or Shop.objects.filter(user__email=request.user.email).exists():
        return redirect('two_app:shop-profile', request.user.username)

    user = CustomUser.objects.get(username=username)

    if Customer.objects.filter(user__username=username).exists():
        text = Customer.objects.filter(user__username=username).values_list('description', flat=True).get()
    else:
        # Create new customer user here
        text = Customer.objects.create(user=user, description="First Comment")
        text = text.description

    context = {
        'user': user,
        'text': text
    }
    template = "two_app/customer-profile.html"
    return render(request, template, context)