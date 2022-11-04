from django.db import models

# Create your models here.

class Company(models.Model):
    name = models.CharField(max_length=200)
    bio = models.TextField(max_length=250, null=True, blank=True)

    def __str__(self):
        return self.name

class Advocate(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=500, null=True, blank=True)
    profile_pic = models.ImageField(null=True, blank=True)
    username = models.CharField(max_length=500, null=True, blank=True)
    bio = models.TextField(max_length=550, null=True, blank=True)
    twitter = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.username