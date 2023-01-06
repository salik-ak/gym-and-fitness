from django import forms
from .models import Admissions


class DateInput(forms.DateInput):
    input_type = 'date'


class AdmissionForm(forms.ModelForm):
    class Meta:
        model = Admissions
        fields = '__all__'

        widgets = {
            'admission_date': DateInput(),

        }
        labels = {
            's_name': 'Student Name: ',
            's_phone': 'Student Phone: ',
            's_email': 'Student Email: ',
            'trainers_name': 'Trainers Name: ',
            'admission_date': 'Admission Date: ',

        }
