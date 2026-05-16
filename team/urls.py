from django.urls import path
from . import views

app_name = 'team'

urlpatterns = [
    path('', views.employee_list, name='employee_list'),
]
