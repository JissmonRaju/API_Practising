from django.shortcuts import render
import requests

# Create your views here.

def new_page(request):
    api_url="https://fakestoreapi.com/products"
    data = requests.get(api_url)
    if data.status_code == 200:
        prod = data.json()
    else:
        prod = []
    return render(request,'NewPage.html',{'prod':prod})

def jewel_prod(request):
    api_url="https://fakestoreapi.com/products/category/jewelery"
    data = requests.get(api_url)
    if data.status_code==200:
        jewel = data.json()
    else:
        jewel = []
    return render(request,'Prod_Jewel.html',{'jewel':jewel})