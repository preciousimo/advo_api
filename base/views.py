from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Advocate

# Create your views here.
@api_view(['GET'])
def endpoints(request):
    data = ['/advocates', 'advocates/:username']
    return Response(data)

@api_view(['GET'])
def advocate_list(request):
    # data = ['Preciousimo', 'Dennis', 'Jolomon']
    advocates = Advocate.objects.all()
    return Response(advocates)

@api_view(['GET'])
def advocate_detail(request, username):
    data = username
    return Response(data)