from django.db import models
from django.contrib.auth.models import User
from django_countries.fields import CountryField
from django.db.models.signals import post_save
from django.dispatch import receiver


class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_image = models.ImageField(null=True, blank=True)
    default_street_address1 = models.CharField(max_length=80, null=True, blank=True)
    default_street_address2 = models.CharField(max_length=80, null=True, blank=True)
    default_town_or_city = models.CharField(max_length=40, null=True, blank=True)
    default_county = models.CharField(max_length=80, null=True, blank=True)
    default_postcode = models.CharField(max_length=20, null=True, blank=True)
    default_country = CountryField(blank_label='Country', null=True, blank=True)

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):

    if created:
        UserProfile.objects.create(user=instance)
        instance.userprofile.save()


DIFFICULTY_OPTIONS = (
        ("Easy", "Easy, all levels of fitness and beginners"),
        ("Medium", "Medium, fair level of fitness, some steep climbs"),
        ("Hard", "Challenging, good level of fitness and experience needed"),
    )


class SuggestChallenge(models.Model):
    name = models.CharField(max_length=254)
    challenge_description = models.TextField()
    challenge_image = models.ImageField(null=True, blank=True)
    challenge_price = models.DecimalField(max_digits=6, decimal_places=2)
    challenge_distance = models.DecimalField(max_digits=6, decimal_places=2)
    challenge_difficulty_rating = models.CharField(max_length=20, choices=DIFFICULTY_OPTIONS, default='Medium')
    challenge_ascent = models.DecimalField(max_digits=6, decimal_places=2)
    challenge_estimate_time = models.DecimalField(max_digits=6, decimal_places=2)
    challenge_award_name = models.CharField(max_length=254)
    challenge_award_image = models.ImageField(null=True, blank=True)
    challenge_notes = models.TextField(null=True, blank=True)
    challenge_location = models.CharField(max_length=254)
    challenge_start_point = models.CharField(max_length=254)
    challenge_carpark = models.CharField(max_length=254)
    Route_Step_1 = models.TextField()
    Route_Step_2 = models.TextField(null=True, blank=True)
    Route_Step_3 = models.TextField(null=True, blank=True)
    Route_Step_4 = models.TextField(null=True, blank=True)
    Route_Step_5 = models.TextField(null=True, blank=True)
    Route_Step_6 = models.TextField(null=True, blank=True)
    Route_Step_7 = models.TextField(null=True, blank=True)
    Route_Step_8 = models.TextField(null=True, blank=True)
    map_image = models.ImageField(null=True, blank=True)
    recommended_map = models.CharField(max_length=254)

    def __str__(self):
        return self.name
