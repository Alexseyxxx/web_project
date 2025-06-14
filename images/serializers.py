from rest_framework import serializers
from .models import Images


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Images
        fields = ["id", "image", "user"]
        read_only_fields = ["id", "user"]