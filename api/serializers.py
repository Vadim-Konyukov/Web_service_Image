from rest_framework import serializers


class ImageUploadSerializer(serializers.Serializer):
    """
    Serializer для загрузки изображений
    """

    image = serializers.ImageField()
    width = serializers.IntegerField(required=False)
    height = serializers.IntegerField(required=False)
    quality = serializers.IntegerField(required=False, max_value=100, min_value=1)
    watermark = serializers.BooleanField(default=False)
    position = serializers.CharField(required=False)
    opacity = serializers.FloatField(required=False)
