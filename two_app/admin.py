from django.contrib import admin
from .models import CustomUser, Shop, Customer

admin.site.register(CustomUser)
admin.site.register(Shop)
admin.site.register(Customer)
