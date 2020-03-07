from django.db import models

# Create your models here.

class Demenagement(models.Model):
    FORMULE = (
        ('F1', '1 Camion + 2 déménageurs'),
        ('F2', '1 Camion + 3 déménageurs'),
        ('F3', 'Formule Standard'),
        ('F4', 'Formule Confort'),
        ('F5', 'Formule Prestige'),
    )
    date = models.DateField(auto_now_add=True, verbose_name="Date du déménagement")
    volume = models.IntegerField(blank=False, null=False)
    formule = models.CharField(max_length=2, choices=FORMULE, default="F3", verbose_name="Formule choisie")
    commentaire = models.TextField(max_length=200)

    def __str__(self):
        return "Le déménagement du %s , %s, %s." %(self.date, self.volume, self.formule,)
    class Meta:
        verbose_name = "Déménagement"
        verbose_name_plural = "Déménagements"
        ordering = ['date']
    

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
    option = models.CharField(max_length=4, choices=OPTIONS, default="OPT3", verbose_name="options supplémentaires")
    demenagements = models.ManyToManyField(Demenagement, db_column='demenagement_id', related_name='option', blank=True)

    def __str__(self):
        return "L'option: %s => %s" %(self.option, self.get_option_display())
    class Meta:
        verbose_name = "option supplémentaire"
        verbose_name_plural = "options supplémentaires"


class TypeAdresse(models.Model):
    ADRESSES = (
        ("DEPART", "Adresse de départ"),
        ("ARRIVEE", "Adresse d'arrivée"),
    )
    adresse = models.CharField(max_length=10, choices=ADRESSES, default="DEPART")

    def __str__(self):
        return "L'adresse: %s => %s" %(self.adresse, self.get_adresse_display())
    class Meta:
        verbose_name = "Départ/Arrivée"


class Address(models.Model):
    rue = models.CharField("Rue", max_length=100, blank=False) # Google autocomplate
    code_postale = models.CharField("Code postale", max_length=10) #auto
    ville = models.CharField("Ville", max_length=20) #auto
    pays = models.CharField("pays", max_length=20)
    etage = models.IntegerField("Numéro d'étage", blank=False)  # menu déroulant
    ascenceur = models.BooleanField("Ascenceur", default=True) # menu déroulant
    demenagement = models.ForeignKey(Demenagement, db_column='demenagement_id', on_delete=models.CASCADE)
    type_adresse = models.ForeignKey(TypeAdresse, db_column='type_adresse_id', on_delete=models.CASCADE)

    def __str__(self):
        return "%s %s %s: %s" %(self.rue, self.postal_code, self.ville, self.type_adresse)
    class Meta:
        verbose_name = "Adresse"
        verbose_name_plural = "Adresses"


class Prospect(models.Model):
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)
    email     = models.EmailField()
    phone= models.IntegerField(blank=False, null=False)

    def __str__(self):
        return " %s %s" %(self.first_name, self.last_name)
    class Meta:
        verbose_name = "Prospect"
        verbose_name_plural = "Prospects"


class Devis(models.Model):
    date = models.DateField(verbose_name="Date de demande du devis", auto_now_add=True)
    reference = models.IntegerField(default="Ref N°: 00-DEV-16022020")
    contactee = models.BooleanField(default=False)
    traitee = models.BooleanField(default=False)
    disponible = models.BooleanField(default=True)
    prospect = models.ForeignKey(Prospect, on_delete=models.CASCADE)
    #demenagement = models.OneToOneField(Demenagement, on_delete=models.CASCADE)

    def __str__(self):
        return self.reference
    class Meta:
        verbose_name = "Devis"
        verbose_name_plural = "Devis"












"""
#demenagements = models.ManyToManyField(Demenagement, through="DemenagementOptionSupplementaire")
class DemenagementOptionSupplementaire(models.Model):
    demenagement = models.ForeignKey(Demenagement, on_delete=models.CASCADE)
    option_supplementaire = models.ForeignKey(OptionSupplementaire, on_delete=models.CASCADE)
"""



"""
dem1 = Relocation(volume = 45).save()
dem2 = Relocation(volume = 55, formula="F5").save()
dem3 = Relocation(volume = 45, formula="F1").save()
dem4 = Relocation(volume = 25, formula="F4").save()
dem5 = Relocation(volume = 65, formula="F2").save()

departure = AddressCategory.objects.create()
arrival = AddressCategory.objects.create(departure_arrival="ARRIVAL")



address1 = Address.objects.create(street_line= "12 résidence les taratres", postal_code= "92500", city= "Rueil Malmaison", floor= 6, elevator= False, relocation= dem1, address_category= departure )
address2 = Address.objects.create(street_line= "10 Quai de Bercy", postal_code= "75012", city= "Paris", floor= 4, elevator= True, relocation= dem1, address_category= arrival )

address3 = Address.objects.create(street_line= "210 Rue Saint-Maur", postal_code= "75015", city= "Paris", floor= 12, elevator= True, relocation= dem2, address_category= departure )
address4 = Address.objects.create(street_line= "31 Rue Bara", postal_code= "92130", city= "Issy-les-Moulineaux", floor= 7, elevator= True, relocation= dem2, address_category= arrival )

address5 = Address.objects.create(street_line= "41 Rue Barathon", postal_code= "03100", city= "Montluçon", floor= 1, elevator= False, relocation= dem3, address_category= departure )
address6 = Address.objects.create(street_line= "21 Rue Baratte Cholet", postal_code= "94100", city= "Saint-Maur-des-Fossés", floor= 9, elevator= False, relocation= dem3, address_category= arrival )

address7 = Address.objects.create(street_line= "56 Rue de Cholet", postal_code= "34070", city= "Montpellier", floor= 8, elevator= True, relocation= dem4, address_category= departure )
address8 = Address.objects.create(street_line= "9 Rue de l'Étoile", postal_code= "75017", city= "Paris", floor= 11, elevator= False, relocation= dem4, address_category= arrival )

address9 = Address.objects.create(street_line= "93 Rue de la Butte Verte", postal_code= "93160", city= "Noisy-le-Grand", floor= 3, elevator= False, relocation= dem5, address_category= departure )
address10 = Address.objects.create(street_line= "2 Rue de la Chistera", postal_code= "45380", city= "La Chapelle-Saint-Mesmin", floor= 5, elevator= True, relocation= dem5, address_category= arrival )



supplement1= PackageOptions.object.Create(comments= "les options supplémentaires du dem1", relocation= dem1)
supplement2= PackageOptions.object.Create(comments= "les options supplémentaires du dem2", relocation= dem2)
supplement3= PackageOptions.object.Create(comments= "les options supplémentaires du dem3", relocation= dem3)
supplement4= PackageOptions.object.Create(comments= "les options supplémentaires du dem4", relocation= dem4)
supplement5= PackageOptions.object.Create(comments= "les options supplémentaires du dem5", relocation= dem5)

client1 = Customer.object.Create(first_name= "Coulibaly", last_name= "Souleymane",  email= "s.coulibaly@outlook.com", phone= 33669444719)
client2 = Customer.object.Create(first_name= "Koné", last_name= "Siata",  email= "konesiata.ks@gmail.com", phone= 33669444720)
client3 = Customer.object.Create(first_name= "Nadine", last_name= "Lemorvan",  email= "essorr.contact@gmail.com", phone= 33669444721)
client4 = Customer.object.Create(first_name= "Coulibaly", last_name= "Andréa",  email= "s.coulibaly@outlook.com", phone= 33669444749)
client5 = Customer.object.Create(first_name= "Ouattara", last_name= "Mohamed",  email= "essorr.contacts@gmail.com", phone= 33669444755)

devis1= EstimateRequest.object.Create(customer= client1 , relocation= dem1)
devis2= EstimateRequest.object.Create(customer= client2 , relocation= dem2)
devis3= EstimateRequest.object.Create(customer= client3 , relocation= dem3)
devis4= EstimateRequest.object.Create(customer= client4 , relocation= dem4)
devis5= EstimateRequest.object.Create(customer= client5 , relocation= dem5)
"""