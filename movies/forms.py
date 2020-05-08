
from django import forms

from .models import Reviews, Rating, RatingStars


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Reviews
        fields = ("name", "email", "text")


class RatingForm(forms.ModelForm):
    star = forms.ModelChoiceField(
        queryset=RatingStars.objects.all(), widget=forms.RadioSelect(), empty_label=None
    )

    class Meta:
        model = Rating
        fields = ("star",)