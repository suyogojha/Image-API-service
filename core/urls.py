from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name="base/index.html")),
    path('api/', include('api.urls')),
    path('images/', include('images.urls', namespace='images')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
