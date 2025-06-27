from rest_framework import serializers
from .models import ShortenedURL

class ShortenedURLSerializer(serializers.ModelSerializer):
    short_url = serializers.SerializerMethodField()
    class Meta:
        model = ShortenedURL
        fields = ('id', 'original_url', 'short_code', 'short_url', 'created_at', 'click_count')

    def get_short_url(self, obj):
        request = self.context.get('request')
        return request.build_absolute_uri('/') + obj.short_code

class CreateShortenedURLSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShortenedURL
        fields = ('original_url', 'expires_at')