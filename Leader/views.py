from rest_framework import viewsets

from .models import Leader

from .serializers import LeaderSerializers


class LeaderAPIView(viewsets.ModelViewSet):
    serializer_class = LeaderSerializers
    queryset = Leader.objects.all()

