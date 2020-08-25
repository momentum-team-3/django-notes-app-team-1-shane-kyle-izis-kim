from django.db import models

# Create your models here.


class Note(models.Model):
    title = models.CharField(max_length=200, null=False, blank=False)
    body = models.TextField(max_length=10000, null=False, blank=False)

    def __str__(self):
        return f'{self.title} + \n\n + {self.body}'
