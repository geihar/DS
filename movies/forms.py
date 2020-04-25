from django import forms

from .models import Reviews, Rating, RatingStars


class FormRevievs(forms.ModelForm):
    class Meta:
        model = Reviews
        fields = ('name', 'email', 'text')



# class ReviewForm(forms.ModelForm):
#
#     captcha = ReCaptchaField()
#
#     class Meta:
#         model = Reviews
#         fields = ("name", "email", "text", "captcha")
#         widgets = {
#             "name": forms.TextInput(attrs={"class": "form-control border"}),
#             "email": forms.EmailInput(attrs={"class": "form-control border"}),
#             "text": forms.Textarea(attrs={"class": "form-control border"})
#         }


class RatingForm(forms.ModelForm):
    star = forms.ModelChoiceField(queryset=RatingStars.objects.all(),
                                   widget=forms.RadioSelect(), empty_label=None)

    class Meta:
        model = Rating
        fields = ("star",)