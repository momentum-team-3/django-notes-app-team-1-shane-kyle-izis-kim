from django.db import models

# Create your models here.


class Note(models.Model):
    title = models.CharField(max_length=200, null=False, blank=False)
    body = models.TextField(max_length=10000, null=False, blank=False)
    date_time = models.DateTimeField(
        auto_now_add=True, null=False, blank=False)

    def __str__(self):
        return f'{self.title} {self.body}'
