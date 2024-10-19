from django.db import models

class Course(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    max_students = models.IntegerField()

    def __str__(self):
        return self.name

class Student(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    courses = models.ManyToManyField(Course, related_name='students')

    def __str__(self):
        return self.name
