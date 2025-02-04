from django.shortcuts import render
from rest_framework.views import APIView
from StudApp.models import Student
from StudApp.serializers import StudentSerializer
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
@csrf_exempt
def StudentView(request,id=0):
    if request.method == 'GET':
        x = Student.objects.all()
        obj = StudentSerializer(x, many=True)
        return JsonResponse(obj.data, safe=False)
    elif request.method=='POST':
        x = JSONParser().parse(request)
        obj = StudentSerializer(data=x)
        if obj.is_valid():
            obj.save()
            return JsonResponse("Data Saved Successfully..",safe=False)
        else:
            return JsonResponse("Error In Saving Data..!!",safe=False)
    elif request.method=='PUT':
        x = JSONParser().parse(request)
        y = Student.objects.get(StudId=x['StudId'])
        obj = StudentSerializer(y,data=x)
        if obj.is_valid():
            obj.save()
            return JsonResponse("Data Updated Successfully..",safe=False)
        else:
            return JsonResponse("Data Error ..!",safe=False)
    elif request.method=='PATCH':
        x = JSONParser().parse(request)
        y = Student.objects.get(StudId=x['StudId'])
        obj = StudentSerializer(y,data=x)
        if obj.is_valid():
            obj.save()
            return JsonResponse("Data Updated Successfully..",safe=False)
        else:
            return JsonResponse("Data Error ..!",safe=False)
    elif request.method=='DELETE':
        x = Student.objects.get(StudId=id)
        x.delete()
        return JsonResponse("Data Deleted Successfully..",safe=False)

