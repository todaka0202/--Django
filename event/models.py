from django.db import models


class Event(models.Model):
    event_text = models.CharField(max_length=200)

    def __str__(self):
        return self.event_text


class DateChoice(models.Model):
    event_date = models.CharField(max_length=200)

    def __str__(self):
        return self.event_date


# Create your models here.
