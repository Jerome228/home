from django import forms
from .models import Expens, Salary

class ExpensForm(forms.ModelForm):
    
    class Meta:
        model = Expens
        ddate = forms.DateField(widget=forms.DateInput)
        fields = ['title', 'amount', 'ddate', 'person', 'comment']
        widgets = {
            "ddate": forms.DateInput(attrs={'type': 'date'})
        }
       

class SalaryForm(forms.ModelForm):
    
    class Meta:
        model = Salary
        ddate = forms.DateField(widget=forms.DateInput)
        fields = ['amount', 'ddate', 'person', 'comment']
        widgets = {
            "ddate": forms.DateInput(attrs={'type': 'date'})
        }