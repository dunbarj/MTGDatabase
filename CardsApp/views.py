from django.shortcuts import render
from . import models
from . import forms
import json

# Create your views here.
def loadDB(request):
    json_data = open('static/json/AllSets.json') 
    setdata = json.load(json_data) #deserialises it
    #data2 = json.dumps(json_data) #json formatted string
    
    for set in setdata:
        new_set = models.Set()
        new_set.save()
        
        if "name" in setdata[set]:
            new_set.name=setdata[set]["name"]
        if "code" in setdata[set]:
            new_set.code=setdata[set]["code"]
        if "releaseDate" in setdata[set]:
            new_set.releaseDate=setdata[set]["releaseDate"]
        if "border" in setdata[set]:
            new_set.border=setdata[set]["border"]
        if "type" in setdata[set]:
            new_set.settype=setdata[set]["type"]
        if "block" in setdata[set]:
            new_set.block=setdata[set]["block"]
            
        new_set.save()
        
        for card in setdata[set]["cards"]:
            new_card = models.Card()
            new_card.save()
            
            if "name" in card:
                new_card.name = card["name"]
            if "cmc" in card:
                new_card.cmc = card["cmc"]
            if "type" in card:
                new_card.typeString = card["type"]
            if "rarity" in card:
                new_card.rarity = card["rarity"]
            if "text" in card:
                new_card.text = card["text"]
            if "artist" in card:
                new_card.artist = card["artist"]
            if "number" in card:
                new_card.number = card["number"]
            if "layout" in card:
                new_card.layout = card["layout"]
            if "multiverseid" in card:
                new_card.multiverseid = card["multiverseid"]
            if "imageName" in card:
                new_card.imageName = card["imageName"]
            if "id" in card:
                new_card.cardid = card["id"]
            if "manaCost" in card:
                new_card.manaCost = card["manaCost"]
            if "flavor" in card:
                new_card.flavor = card["flavor"]
            if "power" in card:
                new_card.power = card["power"]
            if "toughness" in card:
                new_card.toughness = card["toughness"]
            
            #Set Colors
            if "colors" in card:
                for color in card["colors"]:
                    count = models.Color.objects.filter(color__exact=color).count()
                    if (count < 1):
                        new_color = models.Color(color=color)
                        new_color.save()
                    temp = models.Color.objects.get(color__exact=color)
                    new_card.colors.add(temp)
                
            #Set Types
            if "supertypes" in card:
                for supertype in card["supertypes"]:
                    count = models.Supertype.objects.filter(name__exact=supertype).count()
                    if (count < 1):
                        new_supertype = models.Supertype(name=supertype)
                        new_supertype.save()
                    temp = models.Supertype.objects.get(name__exact=supertype)
                    new_card.supertypes.add(temp)
               
            if "types" in card:
                for cardtype in card["types"]:
                    count = models.Cardtype.objects.filter(name__exact=cardtype).count()
                    if (count < 1):
                        new_type = models.Cardtype(name=cardtype)
                        new_type.save()
                    temp = models.Cardtype.objects.get(name__exact=cardtype)
                    new_card.types.add(temp)

            if "subtypes" in card:
                for subtype in card["subtypes"]:
                    count = models.Subtype.objects.filter(name__exact=subtype).count()
                    if (count < 1):
                        new_subtype = models.Subtype(name=subtype)
                        new_subtype.save()
                    temp = models.Subtype.objects.get(name__exact=subtype)
                    new_card.subtypes.add(temp)

            #Set Set
            new_card.cardset = new_set
            new_card.save()
        new_set.save()
        print "Done with set", setdata[set]["name"]

    json_data.close()
    return render(request, 'index.html')

def cardSearch(request):
	return

def getCards(request):
	return

def getCard(request):
    in_id = request.GET.get('multiverseid', 'None')
    in_card = models.Card.objects.get(multiverseid__exact=in_id)
    othersets = models.Card.objects.filter(name__exact=in_card.name)
    context = {
        'card' : in_card,
        'othersets': othersets,
    }
    return render(request, 'card.html', context)

def simple(request):
	form = forms.SimpleForm(request.POST)
	if form.is_valid():
		term = form.cleaned_data['term']
		cards = models.Card.objects.filter(name__contains=term).order_by('name')
		context = {
			'cards' : cards,
		}
		return render(request, 'index.html', context)