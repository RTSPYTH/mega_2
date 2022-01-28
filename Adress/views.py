from rest_framework import viewsets

from .models import Adress

from .serializers import AdressSerializers


class AdressAPIView(viewsets.ModelViewSet):
    serializer_class = AdressSerializers
    queryset = Adress.objects.all()

