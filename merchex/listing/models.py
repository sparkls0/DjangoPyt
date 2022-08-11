from django.db import models

from django.core.validators import MaxValueValidator, MinValueValidator

class Band(models.Model):
    
    class Genre(models.TextChoices):
        HIP_HOP = 'HH'
        SYNTH_POP = 'SP'
        ALTERNATIVE_ROCK = 'AR'
        
    name = models.fields.CharField(max_length=100, default = ' ')
    genre = models.fields.CharField(max_length=50, default = ' ')
    biography = models.fields.CharField(max_length=1000, default = ' ')
    year_formed = models.fields.IntegerField(
    validators=[MinValueValidator(1900), MaxValueValidator(2022)]
    )
    active = models.fields.BooleanField(default=True)
    official_homepage = models.fields.URLField(null=True, blank=True)
    genre = models.fields.CharField(choices=Genre.choices, max_length=5)
    
    
    
class Listing(models.Model):
    
    class Type(models.TextChoices):
        RECORDS = 'R'
        CLOTHING = 'C'
        POSTERS = 'P'
        MISCELLANOUS = 'M'
    
    name = models.fields.CharField(max_length=100)
    description = models.fields.CharField(max_length=1000)
    sold = models.fields.BooleanField(default= False)
    year = models.fields.IntegerField(validators=[MinValueValidator(1900), MaxValueValidator(2022)], blank=True, null=True)
    type = models.fields.CharField(choices=Type.choices, max_length=10)
    