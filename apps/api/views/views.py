# from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from django.http import JsonResponse


# Create your views here.
def index(request):
    message = {"message": "You have accessed an API resource"}
    return JsonResponse(message, safe=False)

