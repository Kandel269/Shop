from django.http import HttpResponse
from django.shortcuts import render
from .models import Product

# Create your views here.

def index(request):
    request02 = Product.objects.all()
    return HttpResponse(request02)