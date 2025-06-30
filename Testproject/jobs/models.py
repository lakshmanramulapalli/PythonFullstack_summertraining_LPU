from django.db import models

# Create your models here.

class Job(models.Model):
    title = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    salary = models.IntegerField()
    description = models.TextField()

    def __str__(self):
        return self.title