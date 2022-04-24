from allauth.account.views import LoginView
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from two_app.models import CustomUser, Shop, Customer


class ShopSignUp(LoginView):
    template_name = 'two_app/shop-login.html'


class CustomerSignup(LoginView):
    template_name = 'two_app/customer-login.html'


@login_required
def shopProfile(request, username):
    user = CustomUser.objects.get(username=username)

    if Shop.objects.filter(user__username=username).exists():
        text = Shop.objects.filter(user__username=username).values_list('description', flat=True).get()
    else:
        text = Shop.objects.create(user=user, description="First Comment")
        text = text.description
    context = {
        'user': user,
        'text': text
    }
    template = "two_app/shop-profile.html"
    return render(request, template, context)


@login_required
def customerProfile(request, username):
    user = CustomUser.objects.get(username=username)

    if Customer.objects.filter(user__username=username).exists():
        text = Customer.objects.filter(user__username=username).values_list('description', flat=True).get()
    else:
        text = Customer.objects.create(user=user, description="First Comment")
        text = text.description

    context = {
        'user': user,
        'text': text
    }
    template = "two_app/customer-profile.html"
    return render(request, template, context)