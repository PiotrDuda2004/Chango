from django.db import models

class User(models.Model):
      message = models.CharField(max_length=200)
      username = models.CharField(max_length=200)
