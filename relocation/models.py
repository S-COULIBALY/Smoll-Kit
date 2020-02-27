from django.db import models

# Create your models here.

# le Déménagement
class Demenagement(models.Model):
    FORMULE = (
        ('F1', '1 Camion + 2 déménageurs'),
        ('F2', '1 Camion + 3 déménageurs'),
        ('F3', 'Formule Standard'),
        ('F4', 'Formule Confort'),
        ('F5', 'Formule Prestige'),
    )
    date = models.DateField(auto_now_add=True, verbose_name="Date du déménagement") # calendar
    volume = models.IntegerField(blank=False, null=False)
    formule = models.CharField(max_length=2, choices=FORMULE, default="F3", verbose_name="Formule choisie")
    commentaire = models.TextField()

    def __str__(self):
        return self.formule
    class Meta:
        verbose_name = "Déménagement"
        verbose_name_plural = "Déménagements"
        ordering = ['date']


# le catégory d'adresse
class TypeAdresse(models.Model):
    LIEUX = (
        ("DEPART", "Adresse de départ"),
        ("ARRIVEE", "Adresse d'arrivée"),
    )
    lIEU = models.CharField(max_length=10, choices=LIEUX, default="DEPART")

    def __str__(self):
        return self.libellee
    class Meta:
        verbose_name = "Départ/Arrivée"


# la localité
class Address(models.Model):
    rue = models.CharField("Rue", max_length=100, blank=False) # Google autocomplate
    code_postale = models.CharField("Code postale", max_length=10) #auto
    ville = models.CharField("Ville", max_length=20) #auto
    pays = models.CharField("pays", max_length=20)
    etage = models.IntegerField("Numéro d'étage", blank=False)  # menu déroulant
    ascenceur = models.BooleanField("Ascenceur", default=True) # menu déroulant
    demenagement = models.ForeignKey(Demenagement, on_delete=models.CASCADE)
    type_adresse = models.ForeignKey(TypeAdresse, on_delete=models.CASCADE)

    def __str__(self):
        return self.street_line + " " + self.postal_code + " " + self.city + " : " + self.address_category
    class Meta:
        verbose_name = "Adresse"
        verbose_name_plural = "Adresses"



# Les options supplémentaires
class OptionSupplementaire(models.Model):
    OPTIONS = (
        ("OPT1", "parck d'emballage"),
        ("OPT2", "Emballage/Déballage de fragiles"),
        ("OPT3", "Emballage/Déballage de non-fragiles"),
        ("OPT4", "Montage/Démontage"),
        ("OPT5", "Assurance"),
        ("OPT6", "Lourds"),
        ("OPT2", "Emballage/Déballage de fragiles"),
    )
    options = models.CharField(max_length=2, choices=options, default="F3", verbose_name="options supplémentaires")
    commentaire = models.TextField()
    demenagement = models.OneToOneField(Demenagement, on_delete=models.CASCADE)

    def __str__(self):
        return self.heavy_items
    class Meta:
        verbose_name = "option supplémentaire"
        verbose_name_plural = "options supplémentaires"


class DemenagementOptionSupplementaire(models.Model):
    demenagement = models.ForeignKey(Demenagement, on_delete=models.CASCADE)
    option_supplementaire = models.ForeignKey(OptionSupplementaire, on_delete=models.CASCADE)


# Les infos Personnelle
class Prospect(models.Model):
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)
    email     = models.EmailField()
    phone= models.IntegerField(blank=False, null=False)

    def __str__(self):
        return self.first_name + " " + self.last_name
    class Meta:
        verbose_name = "Prospect"
        verbose_name_plural = "Prospects"


#  Demande d'estimation
class DemandeDevis(models.Model):
    date = models.DateField(verbose_name="Date de demande du devis", auto_now_add=True)
    reference = models.IntegerField(default="Ref N°: 00-DEV-16022020")
    contactee = models.BooleanField(default=False)
    traitee = models.BooleanField(default=False)
    disponible = models.BooleanField(default=True)
    prospect = models.ForeignKey(Prospect, on_delete=models.CASCADE)
    demenagement = models.OneToOneField(Demenagement, on_delete=models.CASCADE)

    def __str__(self):
        return self.reference
    class Meta:
        verbose_name = "Adresse"
        verbose_name_plural = "Adresses"
