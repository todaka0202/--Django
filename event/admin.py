from django.contrib import admin

from .models import Event
from .models import DateChoice


admin.site.register(Event)
admin.site.register(DateChoice)
