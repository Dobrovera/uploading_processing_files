from .models import File
from rest_framework import serializers


class FileSerializer(serializers.ModelSerializer):
    file = serializers.FileField()

    class Meta:
        model = File
        fields = ('file', 'uploaded_at', 'processed')
