from django.urls import re_path
from StudApp import views

urlpatterns=[
    re_path(r'^student/$',views.StudentView),
    re_path(r'^student/([0-9]+)/$', views.StudentView),

]

