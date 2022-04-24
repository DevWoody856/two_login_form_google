from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView


urlpatterns = [
    path('', TemplateView.as_view(template_name='two_app/index.html'), name='home'),
    path('admin/', admin.site.urls),
    path('accounts/', include('two_app.urls')),
    path('accounts/', include('allauth.urls')),
]
