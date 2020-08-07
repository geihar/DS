from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class UserRegForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]


class UserUpdate(forms.ModelForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ["username", "email"]


class ProfileImg(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ProfileImg, self).__init__(*args, **kwargs)
        self.fields["img"].label = "Изображение профиля"

    class Meta:
        model = Profile
        fields = ["img"]
