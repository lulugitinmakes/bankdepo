from django import forms
from django.contrib.auth.forms import UserCreationForm
from bankapp.models import person

class LoginForm(forms.Form):
    Username=forms.CharField(max_length=225)
    Password=forms.CharField(label='Password',widget=forms.PasswordInput)

#register


#form2

class personform(forms.ModelForm):
    class Meta:
        model=person
        fields = '__all__'



