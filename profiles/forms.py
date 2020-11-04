from django import forms
from .models import UserProfile, SuggestChallenge


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        profiles = UserProfile.objects.all()


class SuggestChallengeForm(forms.ModelForm):

    class Meta:
        model = SuggestChallenge
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        suggest_challenge = SuggestChallenge.objects.all()
