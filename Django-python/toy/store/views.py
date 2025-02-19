from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def test(request):
    return HttpResponse('<h1>This is text page</h1>',
                        content_type='text/plain')

def home2(request):
    return render(request,'home2.html')

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def index1(request):
    return render(request, 'index1.html')
# syntax of a full satck webpage
def index(request):
    return render(request,'index.html')

def blog(request):
    return render(request, 'blog.html')

def class1(request):
    return render(request, 'class1.html')

def about(request):
    return render(request, 'about.html')
