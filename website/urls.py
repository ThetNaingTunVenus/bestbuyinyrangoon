from django.urls import path
from .views import *
from . import views
app_name = 'shop'
urlpatterns = [
    path('', TestView.as_view()),
    path('h', homesite),
]

from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
