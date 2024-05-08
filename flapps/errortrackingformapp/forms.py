# forms.py
from django import forms
from .models import TestForm

class TestFormForm(forms.ModelForm):
    class Meta:
        model = TestForm
        fields = ['notes']
