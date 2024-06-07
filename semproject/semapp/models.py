from django.db import models

class User(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, blank=False)
    username = models.CharField(max_length=100,blank=False)
    email = models.EmailField(max_length=100,blank=False,unique=True)
    password = models.CharField(max_length=100,blank=False)

    class Meta:
        db_table = "user_table"