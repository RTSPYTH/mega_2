from rest_framework import viewsets

from .models import Product

from .serializers import ProductSerializers


class ProductAPIView(viewsets.ModelViewSet):
    serializer_class = ProductSerializers
    queryset = Product.objects.all()
