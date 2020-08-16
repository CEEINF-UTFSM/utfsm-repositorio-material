
from rest_framework import serializers
from .models import Ramo


class RamoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ramo
        fields = "__all__"
