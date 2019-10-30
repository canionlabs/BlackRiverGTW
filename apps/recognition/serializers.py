from rest_framework import serializers


class FaceSerializer(serializers.ModelSerializer):
    image = serializers.FileField()

    class Meta:
        model = ImageFace
        exclude = []

