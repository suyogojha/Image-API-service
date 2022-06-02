from django.urls import path
from .views import ImageAPIView
#from . import views

urlpatterns = [
    path('', ImageAPIView.as_view()),
    path('id/<id>', ImageAPIView.as_view()),
    #path('', views.ImageAPI, name='post_single'),
]
