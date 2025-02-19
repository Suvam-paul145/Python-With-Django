from django.urls import path
from . import views
urlpatterns = [
    path('test',views.test),
    path('home2',views.home2),
    path('home',views.home),
    path('about',views.about),
    path('index1',views.index1),
    path('index',views.index),
    path('class1',views.class1),
    path('blog',views.blog),
    path('add',views.add),
    path('addcode',views.addcode),
    path('cal',views.cal),
    path('calculator',views.calculator),
    
    
]
