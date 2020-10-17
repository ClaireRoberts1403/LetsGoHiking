from django.db import models


DIFFICULTY_OPTIONS = (
        ("Easy", "Easy, all levels of fitness and beginners"),
        ("Medium", "Medium, fair level of fitness, some steep climbs"),
        ("Hard", "Challenging, good level of fitness and experience needed"),
    )


class challenge(models.Model):
    name = models.CharField(max_length=254)
    challenge_description = models.TextField()
    challenge_image = models.ImageField(null=True, blank=True)
    challenge_price = models.DecimalField(max_digits=6, decimal_places=2)
    challenge_distance = models.DecimalField(max_digits=6, decimal_places=2)
    challenge_difficulty_rating = models.CharField(max_length=20, choices=DIFFICULTY_OPTIONS, default='Medium')
    challenge_ascent = models.DecimalField(max_digits=6, decimal_places=2)
    challenge_descent = models.DecimalField(max_digits=6, decimal_places=2)
    challenge_estimate_time = models.DecimalField(max_digits=6, decimal_places=2)
    challenge_award_name = models.CharField(max_length=254)
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
