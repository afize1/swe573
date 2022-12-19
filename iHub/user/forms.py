from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, SetPasswordForm
from django.db.models.query import RawQuerySet

from user.models import shares


DEMO_CHOICES =(
    ("1", "What is your favorite color"),
    ("2", "What is your favorite book name"),
    ("3", "What is your favorite song name"),
)

PRIVATE_CHOICES =(
    ("1", "Private"),
    ("2", "Public"),
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

class UserForm(forms.ModelForm):
    subject= forms.CharField(required=True)
    label = forms.CharField(required=True)
    private = forms.ChoiceField(choices=PRIVATE_CHOICES, required=True)
    value=forms.CharField(max_length=255)
    comment = forms.CharField(max_length=255, required=False)
    class Meta:
        model = User
        fields = ['subject', 'label','private', 'value','comment']

class UpdateUserForm(forms.ModelForm):
    first_name = forms.CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=100,
                                required=True,
                                widget=forms.TextInput(attrs={'class': 'form-control'}))
    occupation = forms.CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    interest = forms.CharField(max_length=100,
                               required=True,
                             widget=forms.TextInput(attrs={'class': 'form-control'}))
    bio = forms.CharField(max_length=100,
                          required=True,
                             widget=forms.TextInput(attrs={'class': 'form-control'}))
    image = forms.ImageField()
    class Meta:
        model = User
        fields = ['first_name', 'last_name','occupation', 'interest','bio','image',]

class CommentForm(forms.ModelForm):
    comment = forms.CharField(max_length=255)
    class Meta:
        model = User
        fields = ['comment']