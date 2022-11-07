from django.contrib.auth.forms import UserCreationForm
from django import forms

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ("email",)

class StudForm(forms.Form):
    Name = forms.CharField(max_length=30)
    Classroom = forms.CharField(max_length=30)
    Address = forms.CharField(max_length=30)
    School = forms.CharField(max_length=30)
    Email = forms.EmailField(max_length=30)

class SForm(forms.Form):
    Name = forms.CharField(max_length=30)