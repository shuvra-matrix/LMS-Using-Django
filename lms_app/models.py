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

class Create_assignment(models.Model):
    id = models.AutoField(primary_key=True)
    admin_id = models.IntegerField(unique=False)
    title = models.CharField(max_length=100,unique=False)
    department = models.CharField(max_length=100, unique=False)
    subject = models.CharField(max_length=100, unique=False)
    despription = models.CharField(max_length=700,unique=False)
    deadline_date = models.CharField(max_length=50,unique=False)
    deadline_time = models.CharField(max_length=50,unique=False)
    uploaded_date = models.DateTimeField(auto_now_add=True, null=True)
    file = models.CharField(max_length=500,unique=False)


class Student(models.Model):
    id= models.AutoField(primary_key=True)
    name = models.CharField(max_length=70,unique=False)
    course = models.CharField(max_length=70,unique=False)
    department = models.CharField(max_length=100, unique=False)
    reg_no = models.CharField(max_length=30,unique=True)
    roll_no = models.CharField(max_length=50,unique=True)
    year = models.CharField(max_length=20,unique=False)
    semester = models.CharField(max_length=20,unique=False)
    address = models.CharField(max_length=500,unique=False)

class Submit(models.Model):
    id = models.AutoField(primary_key=True)
    assignment_id = models.IntegerField(unique=False)
    name = models.CharField(max_length=70,unique=False)
    reg_no = models.CharField(max_length=30, unique=False)
    roll_no = models.CharField(max_length=50, unique=False)
    department = models.CharField(max_length=100, unique=False)
    file = models.CharField(max_length=500, unique=False)
    uploaded_date = models.DateTimeField(auto_now_add=True, null=True)
    
    
