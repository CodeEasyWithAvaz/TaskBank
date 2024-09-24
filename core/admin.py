from django.contrib import admin
from .models import OperationType, Operation, OperationTransaction

admin.site.register(OperationType)
admin.site.register(Operation)
admin.site.register(OperationTransaction)