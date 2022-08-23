from curses import termattrs
from email.policy import default
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.core.files.storage import FileSystemStorage

class Band(models.Model):
    
    
    def __str__(self):
        return f'{self.name}'
    
    fs = FileSystemStorage(location = '/static/pictures')
    
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
    url = models.fields.CharField(max_length=200, default='')
    
    
    
class Listing(models.Model):
    
    band = models.ForeignKey(Band, null=True, on_delete=models.SET_NULL)
    
    
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
    