from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import FileUploadParser, FormParser

from .models import File
from .serializers import FileSerializer


class FileUploadView(APIView):
    queryset = File.objects.all()
    serializer_class = FileSerializer
    parser_classes = (FileUploadParser, FormParser,)

    def post(self, request):
        file = request.data('file')
        print(file)
        values = File.objects.all().values()
        return Response({'all_files': list(values)})


class FileGetView(APIView):
    queryset = File.objects.all()
    serializer_class = FileSerializer

    def get(self, request):
        values = File.objects.all().values()
        return Response({'all_files': list(values)})
