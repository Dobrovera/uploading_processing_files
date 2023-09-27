from .models import File
from rest_framework import serializers


class FileSerializer(serializers.Serializer):
    class Meta:
        model = File
        fields = ('file', 'uploaded_at')

