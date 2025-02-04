from django.shortcuts import render
from LibApp.models import Library
from LibApp.serializers import LibrarySerializer
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import default_storage



# Create your views here.

@csrf_exempt
def LibView(request,id=0):
    if request.method == 'GET':
        x = Library.objects.all()
        obj = LibrarySerializer(x,many=True)
        return JsonResponse(obj.data,safe=False)
    elif request.method=='POST':
        x = JSONParser().parse(request)
        obj = LibrarySerializer(data=x)
        if obj.is_valid():
            obj.save()
            return JsonResponse("Data Saved Successfully..",safe=False)
        else:
            return JsonResponse("Error In Saving Data..!!",safe=False)
    elif request.method=='PUT':
        x = JSONParser().parse(request)
        y = Library.objects.get(StudId=x['StudId'])
        obj = LibrarySerializer(y,data=x)
        if obj.is_valid():
            obj.save()
            return JsonResponse("Data Updated Successfully..",safe=False)
        else:
            return JsonResponse("Data Error ..!",safe=False)
    elif request.method=='PATCH':
        x = JSONParser().parse(request)
        y = Library.objects.get(StudId=x['StudId'])
        obj = LibrarySerializer(y,data=x)
        if obj.is_valid():
            obj.save()
            return JsonResponse("Data Updated Successfully..",safe=False)
        else:
            return JsonResponse("Data Error ..!",safe=False)
    elif request.method=='DELETE':
        x = Library.objects.get(StudId=id)
        x.delete()
        return JsonResponse("Data Deleted Successfully..",safe=False)

@csrf_exempt
def save_image(request):
    img = request.FILES['image']
    obj = default_storage.save(img.name,img)
    return JsonResponse(obj,safe=False)

