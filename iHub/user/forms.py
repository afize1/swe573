from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, SetPasswordForm


DEMO_CHOICES =(
    ("1", "What is your favorite color"),
    ("2", "What is your favorite book name"),
    ("3", "What is your favorite song name"),
)


SUBJECT_CHOICES =(
    ("1", "Yoga"),
    ("2", "Sport"),
    ("3", "Film"),
)

LABEL_CHOICES =(
    ("1", "Yoga_label"),
    ("2", "Sport_label"),
    ("3", "Film_label"),
)

TYPE_CHOICES =(
    ("1", "URL"),
    ("2", "Picture"),
    ("3", "Pdf"),
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
    subject= forms.ChoiceField(choices=SUBJECT_CHOICES, required=True)
    label = forms.ChoiceField(choices=LABEL_CHOICES, required=True)
    private = forms.ChoiceField(choices=PRIVATE_CHOICES, required=True)
    type = forms.ChoiceField(choices=TYPE_CHOICES, required=True)
    related_subjects = forms.ChoiceField(choices=SUBJECT_CHOICES, required=True)
    value=forms.CharField(max_length=20)
    comment = forms.CharField(max_length=20)
    class Meta:
        model = User
        fields = ['subject', 'label','private', 'type','related_subjects', 'value','comment']