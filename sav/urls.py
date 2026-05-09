from django.urls import path
from . import views

app_name = 'sav'

urlpatterns = [
    path('', views.intervention_request, name='intervention_request'),
    path('merci/', views.intervention_success, name='intervention_success'),
]
