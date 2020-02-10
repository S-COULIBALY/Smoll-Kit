from django.db import models

# Create your models here.

# le Déménagement
class RelocationInfo(models.Model):
    date = models.DateField() # calendar
    volume = models.IntegerField(blank=False, null=False)
    comments = models.TextField()

    def __str__(self):
        return self.volume

# la localité
class Location(models.Model):
    street_line = models.CharField(max_length=100) # Google autocomplate
    postal_code = models.CharField(max_length=10) #auto
    city = models.CharField(max_length=20) #auto
    floor = models.IntegerField()  # menu déroulant
    elevator = models.CharField(max_length=20) # menu déroulant

# le catégory d'adresse
class LocationCategory(models.Model):
    Pick_up = models.CharField(max_length=10)
    Delivery = models.CharField(max_length=10)

    def __str__(self):
        return self.Pick_up

# Les options supplémentaires
class Removal_Options(models.Model):
    packaging_supplies = models.BooleanField("Fournitures d'emballage", default=False)
    packing_unpacking_fragiles = models.BooleanField("Emballage/Déballage d'objets fragiles", default=False)
    packing_unpacking_non_fragiles = models.BooleanField("Emballage/Déballage d'objets non fragiles", default=False)
    disassembly_assembly = models.BooleanField("Démontage/remontage", default=False)
    moving_insurance = models.BooleanField("Assurance déménagement", default=False)
    heavy_items = models.BooleanField("Objets lourds", default=False)

    def __str__(self):
        return self.heavy_items

# Les infos Personnelle
class Customer(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email     = models.EmailField()
    telephone= models.IntegerField(blank=False, null=False)

    def __str__(self):
        return self.first_name + "" + self.last_name

























# Les objets lourds
class Heavy_Items(models.Model):
    nom = models.CharField(max_length=60, default= "objets lourds")
    frigo_standard = models.BooleanField()
    frigo_americain = models.BooleanField()
    gros_meuble = models.BooleanField()
    piano_droit = models.BooleanField()
    piano_a_queue = models.BooleanField()
    def __str__(self):
        return self.nom