from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView

urlpatterns = [
    path('', TemplateView.as_view(template_name='main.html'), name='main'),
    path('options', TemplateView.as_view(template_name='options.html'), name='options'),
    path('accounts_users/', include('accounts_users.urls')),
    path('accounts_reservations/', include('accounts_reservations.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
]
