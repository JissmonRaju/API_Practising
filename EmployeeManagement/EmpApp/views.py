from django.http import JsonResponse
from django.shortcuts import render

from EmpApp.models import EmployeeDB
from EmpApp.serializers import EmployeeSerializers


# Create your views here.

def Employee_get(request):
    if request.method=='GET':
        x = EmployeeDB.objects.all()
        obj = EmployeeSerializers(x,many=True)
        return JsonResponse(obj.data,safe=False)