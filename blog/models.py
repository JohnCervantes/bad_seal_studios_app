from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.


class Blog(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    pub_date = models.DateField(default=timezone.now)
    body = models.TextField()
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:200] + ' [. . .]'

    def date(self):
        return self.pub_date.strftime('%b %e %Y')

    def get_absolute_url(self):
        return reverse('blog_details', kwargs={'pk': self.pk})
