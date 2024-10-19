from django.db import models
from courses.models import Course

class Teacher(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='teachers')

    def __str__(self):
        return self.name
