from django.urls import path
from .views import ImagesListView

app_name = 'images'

urlpatterns = [
    path('/images', ImagesListView.as_view(), name='images'),
]
