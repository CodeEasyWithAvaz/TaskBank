import random

from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response


class CSITransaction(GenericAPIView):
    def post(self, request, *args, **kwargs):
        request_data = request.data.get("requestData")
        terminal_id = request.data.get("terminalId")
        cur_amount = request.data.get("curAmount")

        response_data = {
            "responseData": {
                "code": 0,
                "reqId": random.randint(1111111, 9999999),
                "paramsList": {
                    "parameter": [
                        {"name": "authorizationNumber", "value": random.randint(1111111, 9999999)},
                        {"name": "approvalCode", "value": random.randint(111111, 999999)},
                        {"name": "rrn", "value": random.randint(1111111111, 9999999999)},
                    ]
                }
            }
        }
        return Response(response_data, status=status.HTTP_200_OK)