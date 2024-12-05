from django import forms
from django.contrib.admin.widgets import AdminDateWidget  # インポート
from .models import Task


class AddTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = "__all__"
        widgets = {"det_date": AdminDateWidget()}
