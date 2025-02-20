from django.shortcuts import render
from django.http import HttpResponse
from store.models import *   # import all classes from models.py
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

def add(request):
    return render(request, 'add.html')

def addcode(request):
    a=int(request.GET['a1'])
    b=int(request.GET['a2'])
    c=a+b
    return render(request,'add.html',{'x':c})

def calculator(request):
    return render(request,'calculator.html')

def cal(request):

    a=int(request.GET['a1'])
    b=int(request.GET['a2'])
    c=a+b
    d=a-b
    e=a*b
    f=a/b
    
    #return HttpResponse(c)
    return render(request,'calculator.html',{'w':c,'x':d,'y':e,'z':f})

def insert(request):
    return render(request, 'insert.html')

def ins(request):
    u = user()
    u.name = request.GET['a1']
    u.mail = request.GET['a2']
    u.password = request.GET['a3']
    u.phno = request.GET['a4']
    u.save()
    return render(request,'insert.html' )

def registration(request):
    return render(request,'registration.html')
    
def reg(request):
    u = registration()
    u.fullname = request.GET['fullname']
    u.username = request.GET['username']
    u.email = request.GET['email']
    u.password = request.GET['password']
    u.save()
    return render(request,'registration.html' )



