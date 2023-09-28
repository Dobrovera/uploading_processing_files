from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser

from .models import File
from .serializers import FileSerializer
from .tasks import process_file


class FileUploadView(APIView):
    queryset = File.objects.all()
    serializer_class = FileSerializer
    parser_classes = (MultiPartParser, FormParser, )

    def post(self, request):
        file = request.FILES.get('file')
        if file:
            file_object = File.objects.create(file=file)
            process_file.apply_async((file_object.id,))
            return Response({'serialize_data': File.objects.filter(id=file_object.id).values()},
                            status=status.HTTP_201_CREATED)


class FileGetView(APIView):
    queryset = File.objects.all()
    serializer_class = FileSerializer

    def get(self, request):
        values = File.objects.all().values()
        return Response({'all_files': list(values)})
