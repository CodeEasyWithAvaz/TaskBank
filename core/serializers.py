from rest_framework import serializers
from .models import Operation, OperationType


class OperationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Operation
        fields = ['id', 'ext_id', 'status']


class CreateOperationSerializer(serializers.ModelSerializer):
    operation_type = serializers.PrimaryKeyRelatedField(queryset=OperationType.objects.all())

    class Meta:
        model = Operation
        fields = ['card_number', 'account', 'amount', 'ext_id', 'operation_type']


