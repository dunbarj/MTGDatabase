from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Format(models.Model):
	name = models.CharField(max_length=20)

class Color(models.Model):
    color = models.CharField(max_length=10)

class Supertype(models.Model):
    name = models.CharField(max_length=10)
    
class Cardtype(models.Model):
    name = models.CharField(max_length=20)
    
class Subtype(models.Model):
    name = models.CharField(max_length=30)
    
class Set(models.Model):
    name = models.CharField(max_length=50, null=True)
    code = models.CharField(max_length=10, null=True)
    releaseDate = models.CharField(max_length=15, null=True)
    border = models.CharField(max_length=7, null=True)
    settype = models.CharField(max_length=15, null=True)
    block = models.CharField(max_length=20, null=True)
    
class Card(models.Model):
    name = models.CharField(max_length=100, null=True)
    manaCost = models.CharField(max_length=40, null=True)
    cmc = models.IntegerField(null=True)
    colors = models.ManyToManyField(Color, related_name="colors")
    typeString = models.CharField(max_length=100, null=True)
    supertypes = models.ManyToManyField(Supertype, related_name="supertypes")
    types = models.ManyToManyField(Cardtype, related_name="types")
    subtypes = models.ManyToManyField(Subtype, related_name="subtypes")
    rarity = models.CharField(max_length=20, null=True)
    text = models.CharField(max_length=400, null=True)
    flavor = models.CharField(max_length=400, null=True)
    artist = models.CharField(max_length=30, null=True)
    number = models.CharField(max_length=4, null=True)
    power = models.CharField(null=True, max_length=2)
    toughness = models.CharField(null=True, max_length=2)
    layout = models.CharField(max_length=20, null=True)
    multiverseid = models.IntegerField(null=True)
    imageName = models.CharField(max_length=50, null=True)
    cardid = models.CharField(max_length=50, null=True)
    cardset = models.ForeignKey(Set, on_delete=models.CASCADE, related_name="cards", null=True)
    
    def __str__(self):
		return self.name