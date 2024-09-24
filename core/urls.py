from django.urls import path
from .views import CreateOperationView, ConfirmOperationView, ABSView, CSIView
urlpatterns = [
    path('create_operation', CreateOperationView.as_view()),
    path('confirm_operation', ConfirmOperationView.as_view()),
    path('abs_request', ABSView.as_view()),
    path('csi_request', CSIView.as_view()),
]
