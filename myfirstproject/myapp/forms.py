from django import forms
from .models import Registration


class RegForm(forms.ModelForm):

    class Meta:

        model = Registration
        # fields = ('name','email')
        fields = '__all__'
