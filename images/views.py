from django.views.generic import ListView
from .models import Images


class ImagesListView(ListView):
    model = Images
    template_name = 'images/show_all.html'
