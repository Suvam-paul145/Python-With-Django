from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def test(request):
    return HttpResponse('<h1>This is text page</h1>',
                        content_type='text/plain')