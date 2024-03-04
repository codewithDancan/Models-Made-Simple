from django.urls import path
from . import views

urlpatterns = [
    path('', views.my_post, name='my_post'),
]
