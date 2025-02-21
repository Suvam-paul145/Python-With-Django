from django.db import models


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



class user4(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField ()
    password = models.CharField(max_length=50)
    phno = models.IntegerField()
    class Meta:
        db_table = "user4"