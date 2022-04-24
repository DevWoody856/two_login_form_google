from uuid import uuid4
from django.db import models
from django.utils import timezone
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.base_user import BaseUserManager
import allauth
from allauth.socialaccount.models import SocialLogin
from allauth.account.utils import get_next_redirect_url
from allauth.utils import get_request_param


@classmethod
def state_from_request(cls, request):
    state = {}
    next_url = get_next_redirect_url(request)
    # # add this statement is important. We get the query parameter we added to the template and store it here as a  session value.
    request.session["user_type"] = get_request_param(request, "user", None)

    if next_url:
        state["next"] = next_url
    state["process"] = get_request_param(request, "process", "login")
    state["scope"] = get_request_param(request, "scope", "")
    state["auth_params"] = get_request_param(request, "auth_params", "")

    return state

allauth.socialaccount.models.SocialLogin.state_from_request = state_from_request




class UserManager(BaseUserManager):
    def create_user(self, username, email, password=None):
        if not email:
            raise ValueError('mail address is required')

        email = self.normalize_email(email)
        user = self.model(username=username, email=email)

        user.set_password(password)
        user.save(using = self._db)

        return user

    def create_superuser(self, username, email, password):

        user = self.create_user(username, email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user


class CustomUser(AbstractBaseUser):
    userId = models.CharField(
        max_length=255, default=uuid4, primary_key=True, editable=False, unique=True)
    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField(unique=True)
    created = models.DateTimeField(default=timezone.now)

    is_shop = models.BooleanField(default=False)
    is_customer = models.BooleanField(default=False)

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.email

    def has_module_perms(self, app_label):
        return self.is_superuser

    def has_perm(self, perm, obj=None):
        return self.is_superuser


class Shop(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    description = models.CharField(max_length=255)

    def __str__(self):
        return self.user.email


class Customer(models.Model):
    user = models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    description = models.CharField(max_length=255)

    def __str__(self):
        return self.user.email