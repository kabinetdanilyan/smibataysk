from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('like/<int:product_id>/', views.like_product, name='like_product'),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)