from rest_framework import serializers

from .models import Adress


class AdressSerializers(serializers.ModelSerializer):
    class Meta:
        model = Adress
        fields = '__all__'
