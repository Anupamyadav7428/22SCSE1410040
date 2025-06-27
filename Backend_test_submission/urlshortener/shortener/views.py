from rest_framework import generics, permissions
from rest_framework.response import Response
from .models import ShortenedURL
from .serializers import ShortenedURLSerializer, CreateShortenedURLSerializer
from django.shortcuts import redirect, get_object_or_404

class ShortenedURLListCreateView(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = ShortenedURLSerializer

    def get_queryset(self):
        return ShortenedURL.objects.filter(created_by=self.request.user)

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return CreateShortenedURLSerializer
        return ShortenedURLSerializer

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

def redirect_to_original(request, short_code):
    url = get_object_or_404(ShortenedURL, short_code=short_code)
    url.click_count += 1
    url.save()
    return redirect(url.original_url)