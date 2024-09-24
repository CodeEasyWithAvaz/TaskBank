from django.db import models


class OperationType(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Operation(models.Model):
    STATUS_CHOICES = [
        ('created', 'Created'),
        ('confirmed', 'Confirmed'),
    ]

    card_number = models.CharField(max_length=20)
    account = models.CharField(max_length=20)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    ext_id = models.CharField(max_length=50, unique=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='created')
    operation_type = models.ForeignKey(OperationType, on_delete=models.CASCADE)

    def __str__(self):
        return f"Operation {self.ext_id} - {self.status}"


class OperationTransaction(models.Model):
    operation = models.ForeignKey(Operation, related_name='transactions', on_delete=models.CASCADE)
    transaction_detail = models.TextField()

    def __str__(self):
        return f"Transaction for {self.operation.ext_id}"
