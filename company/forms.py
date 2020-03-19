from django.forms import ModelForm
from django import forms
from .models import Company,CompanyInfo
# from django.utils import timezone

class DateInput(forms.DateInput):
    input_type = 'date'

class CompanyForm(ModelForm):
    # deadline = forms.DateField(input_formats = '%m/%d/%Y')
    # when = forms.DateField(input_formats = '%m/%d/%Y')
    class Meta:
        model = Company
        exclude = ['user']
        #forms.CheckboxInput(attrs={'class': 'check'})
        widgets = {
            'deadline': DateInput(),
            }

class CompanyInfoForm(ModelForm):
    # deadline = forms.DateField(input_formats = '%m/%d/%Y')
    # when = forms.DateField(input_formats = '%m/%d/%Y')
    class Meta:
        model = CompanyInfo
        exclude = ['user','company']
        #forms.CheckboxInput(attrs={'class': 'check'})

class SortForm(forms.Form):
    keys = [('','-------'),('deadline','期限'),("position",'ポジション'),("desire",'志望度'),("status",'ステータス')]
    key = forms.ChoiceField(choices=keys[1:],required=True)