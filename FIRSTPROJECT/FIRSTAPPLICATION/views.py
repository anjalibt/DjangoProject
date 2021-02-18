from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    return render(request, 'home.html', {'name': 'Catenantion'})

'''def index(request):
        return HttpResponse('Hello, welcome to our home page')'''
