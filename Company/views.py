from rest_framework import viewsets

from .models import Company

from .serializers import CompanySerializers


class CompanyAPIView(viewsets.ModelViewSet):
    serializer_class = CompanySerializers
    queryset = Company.objects.all()
