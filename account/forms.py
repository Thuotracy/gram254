from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from account.models import NUser
from .models import Profile,Image,Comment


class UserRegistrationForm(UserCreationForm):
  class Meta:
    model=NUser
    fields=('name', 'email', 'password1', 'password2')


class UserLoginForm(forms.ModelForm):
  password=forms.CharField(label='password', widget=forms.PasswordInput)

  class Meta:
    model=NUser
    fields=('email', 'password')

  def clean(self):
    if self.is_valid():
      email=self.cleaned_data['email']
      password=self.cleaned_data['password']

      if not authenticate(email=email, password=password):
        raise forms.ValidationError('invalid cridentials')


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude=['username']
        fields ='__all__'


class CommentForm(forms.ModelForm):
    class Meta:
        model=Comment
        fields='__all__'






