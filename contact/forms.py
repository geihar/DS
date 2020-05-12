from django import forms
from .models import Contacts
from snowpenguin.django.recaptcha3.fields import ReCaptchaField


class ContactsForm(forms.ModelForm):
    captcha = ReCaptchaField()

    class Meta:
        model = Contacts
        fields = ('email', "captcha")
        widgets = {
            'email': forms.TextInput(attrs={'class': 'editContent', 'placeholder': 'Ваш Email...'})
        }
        labels = {'email': ''}