from django.urls import path
from .views import ABSTransaction

urlpatterns = [
    path('transaction', ABSTransaction.as_view()),
]
