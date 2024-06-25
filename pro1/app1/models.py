from django.db import models

# Create your models here.
class Person(models.Model):
    GENDER = [
        ('Male', 'male'),
        ('Female', 'female'),
        ('Others', 'others'),
    ]

    first_name = models.CharField(max_length=34)
    last_name = models.CharField(max_length=34)
    gender = models.CharField(max_length=20, choices=GENDER)
    profile_picture = models.ImageField(upload_to='profiles/')
    Address = models.TextField()
    City = models.CharField(max_length=34)