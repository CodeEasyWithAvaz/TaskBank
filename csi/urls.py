from django.urls import path
from .views import CSITransaction

urlpatterns = [
    path('creditTrans', CSITransaction.as_view()),
]
