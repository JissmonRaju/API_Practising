from datetime import datetime, timedelta

from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from NewApp.models import User
from NewApp.serializers import UserSerializer
from rest_framework.exceptions import AuthenticationFailed
import jwt

# Create your views here.

class Registration(APIView):
    def post(self,request):
        obj = UserSerializer(data=request.data)
        obj.is_valid(raise_exception=True)
        obj.save()
        return Response(obj.data)


class LoginView(APIView):
    def post(self,request):
        email = request.data['email']
        password = request.data['password']
        x = User.objects.filter(email=email).first()
        if x is None:
            raise AuthenticationFailed('User Not Found...!!')
        if not x.check_password(password):
            raise AuthenticationFailed('Incorrect Password..!!')
        payload = {
           'id': x.id,
           'exp': datetime.utcnow() + timedelta(minutes=60),
            'iat': datetime.utcnow()
        }

        token = jwt.encode(payload,'secret',algorithm='HS256')
        response = Response()
        response.set_cookie(key='jwt',value=token,httponly=True)
        response.data={
            'jwt': token
        }
        return response


class UserView(APIView):
    def get(self,request):
        token = request.COOKIES.get('jwt')
        print("Hello", token)
        if not token:
            raise AuthenticationFailed("Authentication Failed..!!")
        try:
            payload = jwt.decode(token,'secret',algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed("Authentication Failed..")
        user = User.objects.filter(id=payload['id']).first()
        obj = UserSerializer(user)
        return Response(obj.data)


class LogoutView(APIView):
    def post(self,request):
        x = Response()
        x.delete_cookie('jwt')
        x.data = {
            "message":"Logged Out Successfully..!!"
        }
        return x



