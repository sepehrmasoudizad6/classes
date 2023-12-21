from django.db import models
from student.models import Student

class Teacher(models.Model):
    username = models.CharField(max_length=20, unique=True)
    password = models.CharField(max_length=100)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    national_code = models.CharField(max_length=10, unique=True)
    school_name = models.CharField(max_length=30, blank=True, null=True)
    biography = models.TextField(null=True, blank=True)

class News(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    title = models.CharField(max_length=60)
    context = models.TextField()

class Exercise(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    title = models.CharField(max_length=60)
    context = models.TextField()
    deadline = models.DateTimeField()
    file = models.FileField(upload_to='../Files/')


