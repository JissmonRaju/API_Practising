from django.urls import path
from WorkApp import views

urlpatterns = [
    path('new/',views.new_page,name='new'),
    path('jewel/',views.jewel_prod,name='jewel'),
]