from django.urls import path
from . import views

urlpatterns = [
    path ('createaccount', views.createaccount, name='createaccount'),
    path ('editaccount', views.editaccount, name='editaccount'),
]