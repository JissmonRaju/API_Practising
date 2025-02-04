from django.urls import path
from NewApp import views


urlpatterns = [

    path('reg/',views.Registration.as_view()),
    path('login/',views.LoginView.as_view()),
    path('user/',views.UserView.as_view()),
    path('logout/',views.LogoutView.as_view())

]