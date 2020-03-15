from django.forms import ModelForm
from django import forms
from .models import Company
# from django.utils import timezone

class DateInput(forms.DateInput):
    input_type = 'date'
    
class CompanyForm(ModelForm):
    # deadline = forms.DateField(input_formats = '%m/%d/%Y')
    # when = forms.DateField(input_formats = '%m/%d/%Y')
    class Meta:
        model = Company
        fields = ['name','status','next','deadline','memo']
        forms.CheckboxInput(attrs={'class': 'check'})
        widgets = {
            'deadline': DateInput(),
            }