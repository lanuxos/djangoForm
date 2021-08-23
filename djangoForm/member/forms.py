from django import forms
from .models import *

class AddMemberForm(forms.ModelForm):
    class DatesInput(forms.DateInput):
        input_type = 'date'
    firstName = forms.CharField(label="First Name", max_length=100, required=False)
    lastName = forms.CharField(label="Last Name", max_length=100, required=False)
    # dob = forms.DateField(label="Date Of Birth", required=False)
    dob = forms.DateField(label="Date Of Birth", required=False, widget=DatesInput())
    workPlace = forms.CharField(label="Work Place", required=False)
    title = forms.CharField(label="Title", max_length=100, required=False)
    tel = forms.CharField(label="Tel", max_length=100, required=False)

    class Meta:
        model = Member
        fields = '__all__'
