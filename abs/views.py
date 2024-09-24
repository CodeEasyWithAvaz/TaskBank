import random

from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response


class ABSTransaction(GenericAPIView):
    def post(self, request, *args, **kwargs):
        documents = request.data.get('documents', [])

        if not documents:
            return Response({
                "code": 1,
                "msg": "No documents provided",
                "responseBody": {}
            }, status=status.HTTP_400_BAD_REQUEST)

        created_documents = []
        for doc in documents:
            transaction_id = random.randint(1111111, 9999999)
            created_documents.append({
                "transactionId": transaction_id,
                "externalId": doc.get("externalId")
            })

        return Response({
            "code": 0,
            "msg": "Успешно",
            "responseBody": {
                "createdDocuments": created_documents
            }
        }, status=status.HTTP_201_CREATED)
