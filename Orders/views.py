from rest_framework import viewsets

from .models import Order

from .serializers import OrderSerializers


class OrderAPIView(viewsets.ModelViewSet):
    serializer_class = OrderSerializers
    queryset = Order.objects.all()
