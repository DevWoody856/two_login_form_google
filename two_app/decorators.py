from django.contrib.auth.decorators import user_passes_test
from two_app.models import Shop, Customer


def shop_required(function=None, redirect_field_name=None):
    def is_shop(u):
        return Shop.objects.filter(user__email=u).exists()
    actual_decorator = user_passes_test(
        is_shop,
        redirect_field_name=redirect_field_name
    )
    if function:
        return actual_decorator(function)
    else:
        return actual_decorator


def customer_required(function=None, redirect_field_name=None):
    def is_customer(u):
        return Customer.objects.filter(user__email=u).exists()
    actual_decorator = user_passes_test(
        is_customer,
        redirect_field_name=redirect_field_name
    )
    if function:
        return actual_decorator(function)
    else:
        return actual_decorator