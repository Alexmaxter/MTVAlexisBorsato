from django.urls import path

from .views import index, mi_template, family_list

urlpatterns = [
    path('', index),
    path('mi-template/<nombre>', mi_template),
    path('family_list/', family_list),
]
