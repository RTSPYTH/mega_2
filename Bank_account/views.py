from rest_framework import viewsets

from .models import BankAccount

from .serializers import BankAccountSerializers


class BankAccountAPIView(viewsets.ModelViewSet):
    serializer_class = BankAccountSerializers
    queryset = BankAccount.objects.all()
