from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
def login(request):

    return JsonResponse({'code': 1, 'status': 'success', 'data':'helloworld'})