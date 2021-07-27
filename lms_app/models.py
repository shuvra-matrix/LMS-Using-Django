from django.db import models

# Create your models here.

class Classes(models.Model):
    class_id = models.AutoField(primary_key=True)
    admin_id = models.IntegerField(unique=False)
    class_link = models.URLField(max_length=600, unique=False)
    department = models.CharField(max_length=100,unique=False)
    subject = models.CharField(max_length=100,unique=False)
    date=models.CharField(max_length=50,unique=False)
    time = models.CharField(max_length=50,unique=False)
