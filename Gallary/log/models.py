from django.db import models

# Create your models here.


class Log(models.Model):
    text = models.CharField(max_length=50)
