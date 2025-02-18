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