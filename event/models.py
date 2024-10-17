from django.db import models

class Event(models.Model):
    event_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField


# Create your models here.
