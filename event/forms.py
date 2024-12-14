from django import forms
from django.contrib.admin.widgets import AdminDateWidget
from .models import Datemodel


class DateForm(forms.ModelForm):
    class Meta:
        model = Datemodel
        fields = ("date_field",)
        widgets = {
            "date_field": AdminDateWidget(),
        }
