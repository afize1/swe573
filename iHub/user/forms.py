from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, SetPasswordForm


DEMO_CHOICES =(
    ("1", "What is your favorite color"),
    ("2", "What is your favorite book name"),
    ("3", "What is your favorite song name"),
)


class UserRegisterForm(UserCreationForm):
    username= forms.CharField(max_length=20)
    first_name = forms.CharField(max_length=20)
    last_name = forms.CharField(max_length=20)
    email = forms.EmailField()
    verify_email=forms.EmailField()
    security_question = forms.ChoiceField(choices=DEMO_CHOICES, required=True)
    answer = forms.CharField(max_length=20)
    class Meta:
        model = User
        fields = ['username','first_name', 'last_name', 'email', 'verify_email', 'password1', 'password2']


class UserChangePasswordForm(forms.Form):
    username= forms.CharField(max_length=20)
    security_question = forms.ChoiceField(choices=DEMO_CHOICES, required=True)
    answer = forms.CharField(max_length=20)
    class Meta:
        model = User
        fields = ['username', 'security_question','answer']
        
class ChangePasswordForm(SetPasswordForm):
    class Meta:
        model = User
        fields = ['new_password1', 'new_password2']