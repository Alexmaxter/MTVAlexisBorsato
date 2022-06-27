from django.urls import path

from .views import index, family_list

urlpatterns = [
    path('', index),
    path('family_list/', family_list)
]
