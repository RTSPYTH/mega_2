from rest_framework import serializers

from .models import Leader


class LeaderSerializers(serializers.ModelSerializer):
    class Meta:
        model = Leader
        fields = '__all__'
