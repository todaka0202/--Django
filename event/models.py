from django.db import models


class Event(models.Model):
    event_text = models.CharField(max_length=200)

    def __str__(self):
        return self.event_text


class Datemodel(models.Model):
    date_field = models.DateField()


# Create your models here.
