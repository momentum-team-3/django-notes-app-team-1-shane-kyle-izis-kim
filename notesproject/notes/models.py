from django.db import models

# Create your models here.


class Notes(models.Model):
    title = models.CharField(max_length=200, null=False, blank=False)
    body = models.CharField(max_length=10000, null=False, blank=False)
