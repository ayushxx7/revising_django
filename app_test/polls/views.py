from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def html_response(request):
    return render(request, 'polls/extended_from_base.html')

