from django.urls import path
from .views import ShortenedURLListCreateView

urlpatterns = [
    path('', ShortenedURLListCreateView.as_view(), name='url-list-create'),
]