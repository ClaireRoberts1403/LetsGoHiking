from django import forms
from .models import challenge


class ChallengeForm(forms.ModelForm):

    class Meta:
        model = challenge
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        challenges = challenge.objects.all()
