from django.forms import ModelForm
from django import forms
from .models import Car, Staff, Assigning,Fuelling, Repair_issues, Repair_records, Service_issues, Service_records

class CarForm(ModelForm):
    class Meta:
        model = Car
        fields = '__all__'
        widgets = {
            'Expiry_insurance': forms.DateInput(attrs={'type': 'date'})}

class StaffForm(ModelForm):
    class Meta:
        model = Staff
        fields = '__all__'

class AssigningForm(ModelForm):
    class Meta:
        model = Assigning
        fields = '__all__'  
        widgets = {
            'assignment_date': forms.DateInput(attrs={'type': 'date'})}

class FuellingForm(ModelForm):
    class Meta:
        model = Fuelling
        fields = '__all__' 
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'})}

class Repair_issuesForm(ModelForm):
    class Meta:
        model = Repair_issues
        fields = '__all__'

class Repair_recordsForm(ModelForm):
    class Meta:
        model = Repair_records
        fields = '__all__'
        widgets = {
            'repair_date': forms.DateInput(attrs={'type': 'date'})}

class Service_issuesForm(ModelForm):
    class Meta:
        model = Service_issues
        fields = '__all__'

class Service_recordsForm(ModelForm):
    class Meta:
        model = Service_records
        fields = '__all__'
        widgets = {
            'service_date': forms.DateInput(attrs={'type': 'date'})
        }
        