from django.db import models
class user(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField 
    password = models.CharField(max_length=50)
    phno = models.IntegerField
    class Meta:
        db_table = "user"

class user2(models.Model):
    fullname = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    email = models.EmailField
    password = models.CharField(max_length=50)
    class Meta: 
        db_table = "user2"

class register(models.Model):
    fullname = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    email = models.EmailField
    password = models.CharField(max_length=50)
    class Meta: 
        db_table = "register"

def endcode(request,id):
    d = register.objects.get(id=id)
    d.name=request.GET['a1']
    d.email=request.GET['a2']
    d.password=request.GET['a3']
    d.phno=request.GET['a4']
    d.save()
    return redirect('../show')