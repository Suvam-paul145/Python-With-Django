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
    path('insert',views.insert),
    path('ins', views.ins),
    path('registration', views.registration),
    path('reg', views.reg),
    path('show', views.show),
    path('del/<int:id>',views.dele),
    path('edit/<int:id>',views.edit),
    path('edcode/<int:id>', views.edcode, name='edcode'),
    path('log2', views.log2, name='log2'),
    path('login', views.login, name='login'),
    path('index_new', views.index_new, name='index_new'),
    path('inset_new', views.inset_new, name='inset_new'),

]
