from django.shortcuts import render
from rest_framework.views import APIView
from StudApp.models import Student
from StudApp.serializers import StudentSerializer
from django.http.response import JsonResponse


# Create your views here.

def StudentView(request):
    if request.method == 'GET':
        x = Student.objects.all()
        obj = StudentSerializer(x, many=True)
        return JsonResponse(obj.data, safe=False)
