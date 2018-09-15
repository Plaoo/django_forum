from django import forms
from djago.contrib.auth.forms import UserCreationForm
from djago.contrib.auth.models import User
class RegistrationForm(UserCreationForm):
    email = forms.CharField(max_length=30, required=True, widget=forms.EmailInput())

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']