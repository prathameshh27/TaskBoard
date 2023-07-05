# from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from django.http import JsonResponse


# Create your views here.
def index(request):
    '''Home-views-views-index'''
    print("\n\n## Home-views-views-index executed ##")
    return JsonResponse({"msg": "Home View"}, safe=False)

