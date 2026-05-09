from django.urls import path
from . import views
app_name = 'showcase'

urlpatterns = [
    path('', views.index, name='index'),
    path('certificates/', views.certificates, name='certificates'),
    path('resources/', views.resources, name='resources'),
    path('about/', views.about, name='about'),
]
