from django.forms import ModelForm
from django import forms
from .models import Reservation

class ReservationForm(ModelForm):
    class Meta:
        model = Reservation
        fields ='__all__'
        widgets = {
            'Date_Check_In': forms.DateInput(attrs={'type': 'date'}),
            'Date_Check_Out': forms.DateInput(attrs={'type': 'date'})
        }