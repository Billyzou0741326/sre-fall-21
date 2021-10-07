from django.db import models
from datetime import date

class HomeItem(models.Model):
    content = models.TextField()
    date_created = models.DateField(default=date.today)
    author = models.TextField(blank=True)

class DoneItem(models.Model):
    content = models.TextField()
    date_completed = models.DateField(default=date.today)
    author = models.TextField(blank=True)
