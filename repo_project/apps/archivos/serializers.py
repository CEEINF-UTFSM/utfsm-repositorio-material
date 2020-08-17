from rest_framework import serializers
from .models import Archivo
from ramos.serializers import RamoSerializer


class ArchivoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Archivo
        fields = ["nombre", "ramo", "tipo",
                  "semestre", "subido", "user", "id", "path"]

    def to_representation(self, instance):
        self.fields['ramo'] = RamoSerializer(read_only=True)
        return super(ArchivoSerializer, self).to_representation(instance)
