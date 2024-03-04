from django.urls import path
from . import views

urlpatterns = [
    path('', views.total_transaction_amount, name ='total_transaction_amount'),
]
