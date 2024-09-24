from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response


from core.gateway import abs_gateway, csi_gateway
from core.models import Operation
from core.serializers import CreateOperationSerializer, OperationSerializer 


class CreateOperationView(GenericAPIView):
    queryset = Operation.objects.all()
    serializer_class = CreateOperationSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        operation = serializer.save(status='created')
        return Response(self.serializer_class(operation).data, status=status.HTTP_201_CREATED)


class ConfirmOperationView(GenericAPIView):
    queryset = Operation.objects.all()
    serializer_class = OperationSerializer

    def post(self, request, *args, **kwargs):
        ext_id = request.data.get('ext_id')
        try:
            operation = self.get_queryset().get(ext_id=ext_id)
            operation.status = 'confirmed'
            operation.save()
            return Response(self.serializer_class(operation).data, status=status.HTTP_200_OK)
        except Operation.DoesNotExist:
            return Response({"error": "Operation not found"}, status=status.HTTP_404_NOT_FOUND)


class ABSView(GenericAPIView):
    def post(self, request):
        data = {
            "externalId": request.data["externalId"],
            "sender": request.data['sender'],
            "receiver": request.data['receiver'],
            "amount": request.data['amount'],
        }
        response = abs_gateway.post(data=data)

        return Response({"success": response})


class CSIView(GenericAPIView):
    def post(self, request):
        data = {
            "extReqId": request.data["extReqId"],
            "idData": request.data['idData'],
            "currency": request.data['currency'],
            "amount": request.data['amount'],
        }
        response = csi_gateway.post(data=data)

        return Response({"success": response})
