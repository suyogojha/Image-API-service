from rest_framework import serializers
from images.models import Images


class ImagesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Images
        fields = ('id', 'image')


""" class ImagesSerializer(serializers.ModelSerializer):

    image_url = serializers.SerializerMethodField('get_image_url')

    class Meta:
        model = Images
        fields = ('id',
                  'image',
                  'image_url')

    def get_image_url(self, obj):
        return obj.image.url """
