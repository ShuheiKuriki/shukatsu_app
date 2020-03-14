from django.forms import ModelForm
from django import forms
from .models import Company
# from django.utils import timezone

class CompanyForm(ModelForm):
    # deadline = forms.DateField(input_formats = '%m/%d/%Y')
    # when = forms.DateField(input_formats = '%m/%d/%Y')
    class Meta:
        model = Company
        fields = ['name','status','memo']
        forms.CheckboxInput(attrs={'class': 'check'})