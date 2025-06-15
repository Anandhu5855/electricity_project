from django.urls import path
from . import views

urlpatterns = [
    path('', views.submit_status, name='submit_status'),
]