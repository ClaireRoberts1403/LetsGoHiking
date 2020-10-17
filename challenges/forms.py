from django import forms
from .models import challenge


class challengeForm(forms.ModelForm):

    class Meta:
        model = challenge
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        challenges = challenge.objects.all()
