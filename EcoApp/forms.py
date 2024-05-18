from django import forms
from .models import *
# from django.forms import ModelChoiceField


class Student_form(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'


class Event_form(forms.ModelForm):
    class Meta:
        model = Event
        fields = '__all__'


class Booking_form(forms.ModelForm):                              
    class Meta:
        model = Booking
        fields = '__all__'



