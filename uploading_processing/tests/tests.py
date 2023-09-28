import io

from rest_framework.test import APITestCase
from PIL import Image
from rest_framework import status


class TestUpload(APITestCase):

    endpoint = '/upload/'

    def generate_photo_file(self):
        file = io.BytesIO()
        image = Image.new('RGBA', size=(50, 50), color=(150, 200, 100))
        image.save(file, 'png')
        file.name = 'test.png'
        file.seek(0)
        return file

    def test_upload_file(self):
        file = self.generate_photo_file()
        data = {
            'file': file
        }
        response = self.client.post(self.endpoint, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
