from django.db import models
from django.utils import timezone


# Create your models here.
class Projects(models.Model):
    author = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/')
    body = models.TextField()
    date_posted = models.DateField(default=timezone.now)
    status = models.CharField(max_length=200)
    summary = models.CharField(max_length=200)
    technologies = models.CharField(max_length=200)
    carousel = models.TextField(null=True,blank=True)

    def __str__(self):
        return self.title
