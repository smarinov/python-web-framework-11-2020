from django.urls import path

from resources.views import pets

urlpatterns = [
    path('', pets, name='pets'),
]