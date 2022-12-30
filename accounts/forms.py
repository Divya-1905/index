from.models import *
from django import forms
class Signupform(forms.ModelForm):
   class Meta: 
     models = User
     fields = '__all__'
class Loginform(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email', 'password']