from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, SetPasswordForm
from .models import users


DEMO_CHOICES =(
    ("1", "What is your favorite color"),
    ("2", "What is your favorite book name"),
    ("3", "What is your favorite song name"),
)

PRIVATE_CHOICES =(
    ("1", "False"),
    ("2", "True"),
)

Value_Type =(
    ("1", "Url"),
    ("2", "Text"),
)

class UserRegisterForm(UserCreationForm):
    username= forms.CharField(max_length=255)
    first_name = forms.CharField(max_length=255)
    last_name = forms.CharField(max_length=255)
    email = forms.EmailField()
    verify_email=forms.EmailField()
    security_question = forms.ChoiceField(choices=DEMO_CHOICES, required=True)
    answer = forms.CharField(max_length=255)
    class Meta:
        model = User
        fields = ['username','first_name', 'last_name', 'email', 'verify_email', 'password1', 'password2']


class UserChangePasswordForm(forms.Form):
    username= forms.CharField(max_length=255)
    security_question = forms.ChoiceField(choices=DEMO_CHOICES, required=True)
    answer = forms.CharField(max_length=255)
    class Meta:
        model = User
        fields = ['username', 'security_question','answer']
        
class ChangePasswordForm(SetPasswordForm):
    class Meta:
        model = User
        fields = ['new_password1', 'new_password2']

class UserForm(forms.ModelForm):
    subject= forms.CharField(max_length=255)
    type=forms.ChoiceField(choices=Value_Type, required=True)
    content=forms.CharField(max_length=255)
    description = forms.CharField(max_length=255, required=False)
    label = forms.CharField(max_length=255)
    private = forms.ChoiceField(choices=PRIVATE_CHOICES, required=True)
    class Meta:
        model = User
        fields = ['subject', 'type','content','description','label','private']
        
class UpdateUserForm(forms.ModelForm):
    first_name = forms.CharField(max_length=255,
                               required=True,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=255,
                                required=True,
                                widget=forms.TextInput(attrs={'class': 'form-control'}))
    occupation = forms.CharField(max_length=255,
                               required=True,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    interest = forms.CharField(max_length=255,
                               required=True,
                             widget=forms.TextInput(attrs={'class': 'form-control'}))
    bio = forms.CharField(max_length=255,
                          required=True,
                             widget=forms.TextInput(attrs={'class': 'form-control'}))
    image = forms.ImageField()
    class Meta:
        model = User
        fields = ['first_name', 'last_name','occupation', 'interest','bio','image'] 
class CommentForm(forms.ModelForm):
    comment = forms.CharField(max_length=255)
    class Meta:
        model = User
        fields = ['comment']