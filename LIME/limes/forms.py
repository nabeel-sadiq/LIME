from django import forms
from .models import Limes

class LimeForm(forms.ModelForm):
  class Meta:
    model = Limes
    fields = ["content"]