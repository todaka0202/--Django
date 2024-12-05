from django.db import models


class Event(models.Model):
    event_text = models.CharField(max_length=200)

    def __str__(self):
        return self.event_text


class Task(models.Model):
    set_date = models.DateField("日程", blank=True, null=True)


# Create your models here.
