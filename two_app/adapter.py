from allauth.account.adapter import DefaultAccountAdapter
from two_app.models import CustomUser
from django.http import HttpResponse
from two_app.models import CustomUser, Customer, Shop
from allauth.exceptions import ImmediateHttpResponse
from allauth.socialaccount.adapter import DefaultSocialAccountAdapter


class SocialAccountAdapter(DefaultSocialAccountAdapter):
    def pre_social_login(self, request, sociallogin):

        user = sociallogin.user

        if request.session["user_type"] == "shop":
            if Customer.objects.filter(user__email=user).exists():
                raise ImmediateHttpResponse(
                    HttpResponse('You already have a Customer account. You cannot signin using Shop Account'))
            pass

        if request.session["user_type"] == "customer":
            if Shop.objects.filter(user__email=user).exists():
                raise ImmediateHttpResponse(
                    HttpResponse('You already have a Shop account. You cannot signin using Customer Account'))
            pass
        pass


class AccountAdapter(DefaultAccountAdapter):

    def get_signup_redirect_url(self, request):

        if request.session["user_type"] == "shop":
            shop_user = CustomUser.objects.get(email=self.request.user)
            shop_user.is_shop = True
            shop_user.save()
            path = '/accounts/shop/{username}/'
            return path.format(username=request.user.username)


        elif request.session["user_type"] == "customer":
            customer_user = CustomUser.objects.get(email=self.request.user)
            customer_user.is_customer = True
            customer_user.save()
            path = '/accounts/customer/{username}/'
            return path.format(username=request.user.username)

        else:
            user = CustomUser.objects.get(email=self.request.user)
            user.delete()
            return HttpResponse("This is an error related to session. The registered USER deleted.")


    def get_login_redirect_url(self, request):

        if request.session["user_type"] == "shop":
            path = '/accounts/shop/{username}/'
            return path.format(username=request.user.username)

        elif request.session["user_type"] == "customer":
            path = '/accounts/customer/{username}/'
            return path.format(username=request.user.username)


        else:
            return HttpResponse('This is an error related to session.')