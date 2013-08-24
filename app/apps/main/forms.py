from django import forms
from main.models import Person

class PersonForm(forms.ModelForm):
    last_name = forms.CharField(required=False)
    class Meta:
        model=Person
        fields = ('name', 'last_name')
