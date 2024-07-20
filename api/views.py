from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import ImageUploadSerializer
from PIL import Image, ImageDraw, ImageFont
import io
import os
from rest_framework.permissions import IsAuthenticated



class ImageProcessView(APIView):
    """
    API для обработки изображений с добавлением водяного знака
    """

    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = ImageUploadSerializer(data=request.data)
        if serializer.is_valid():
            # Загрузка изображения
            image_file = serializer.validated_data['image']
            image = Image.open(image_file)

            # Изменение размера
            width = serializer.validated_data.get('width')
            height = serializer.validated_data.get('height')
            if width and height:
                image = image.resize((width, height), Image.ANTIALIAS)

            # Сжатие
            quality = serializer.validated_data.get('quality', 85)
            img_byte_arr = io.BytesIO()
            image.save(img_byte_arr, format='JPEG', quality=quality)

            # Добавление водяного знака
            if serializer.validated_data.get('watermark'):
                draw = ImageDraw.Draw(image)
                text = "Watermark"
                font = ImageFont.load_default()
                draw.text((10, 10), text,
                          fill=(255, 255, 255, int(255 * (serializer.validated_data.get('opacity', 0.5)))), font=font)

            img_byte_arr.seek(0)
            return Response({'image': img_byte_arr.getvalue()}, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

