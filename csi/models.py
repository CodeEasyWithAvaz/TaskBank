from django.db import models


class Trans(models.Model):
    req_id = models.CharField(max_length=100, unique=True)
    rrn = models.CharField(max_length=100, unique=True)
    approval_code = models.CharField(max_length=100)
