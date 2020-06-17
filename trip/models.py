from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse

class Destinations(models.Model):
    author = models.ForeignKey(get_user_model(), on_delete = models.CASCADE)
    place = models.CharField(max_length = 50)
    location = models.CharField(max_length = 35)
    summary = models.TextField()

    def __str__(self):
      return self.place