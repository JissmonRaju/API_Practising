from django.urls import re_path
from EmpApp import views

urlpatterns = [

    re_path(r'^employee/',views.Employee_get)
]