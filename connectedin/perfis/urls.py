from django.urls import path

from . import views

app_name = 'perfis'
urlpatterns = [
    path('', views.index, name='index')
]
