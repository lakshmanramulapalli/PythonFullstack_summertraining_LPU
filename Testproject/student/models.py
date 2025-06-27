from django.db import models

# Create your models here.
class Student(models.Model):
    roll_number = models.PositiveIntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    age = models.PositiveIntegerField()
    address = models.TextField()




