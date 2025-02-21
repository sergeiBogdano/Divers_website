from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('apply/', views.application_form, name='application_form'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('application/', views.application_form, name='application_form'),
    path('thank_you/', views.thank_you, name='thank_you'),
    path('gallery/', views.gallery, name='gallery')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
