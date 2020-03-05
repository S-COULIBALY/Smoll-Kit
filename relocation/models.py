from django.db import models

# Create your models here.
class OptionSupplementaire(models.Model):
    libelle = models.CharField(db_column='libelle', max_length = 60)

class Demenagement(models.Model):
    date = models.DateTimeField('date')
    commentaire = models.CharField(db_column='commentaire', max_length = 200)
    volume = models.FloatField(db_column='volume', blank=False, null=False)
    option_supplementaires = models.ManyToManyField(OptionSupplementaire)

    def __str__(self):
        return self.formule
    class Meta:
        verbose_name = 'Déménagement'
        verbose_name_plural = 'Déménagements'

class TypeAdresse(models.Model):
    LIBELLES = (
         ('DEPART', 'Adresse de départ'),
         ('ARRIVEE', 'Adresse d\'arrivée'),
    )
    libelle = models.CharField(db_column='libelle', max_length = 60, choices=LIBELLES)

    def __str__(self):
        return self.libellee
    class Meta:
        verbose_name = 'Départ/Arrivée'

class Adresse(models.Model):
    rue = models.CharField(db_column='rue', max_length = 200, blank=False)
    cp = models.CharField(db_column='cp', max_length = 10)
    ville = models.CharField(db_column='ville', max_length = 100, blank=False)
    pays = models.CharField(db_column='pays', max_length = 100)
    etage = models.IntegerField(db_column='etage', default=0)
    ascenceur = models.BooleanField(db_column='ascenceur')
    demenagement = models.ForeignKey(Demenagement, db_column='demenagement_id', on_delete=models.CASCADE)
    type_adresse = models.ForeignKey(TypeAdresse, db_column='type_adresse_id', on_delete=models.PROTECT)

    def __str__(self):
        return f'{self.street_line} {self.cp} {self.ville}: {self.address_category}'
    class Meta:
     verbose_name = 'Adresse'
     verbose_name_plural = 'Adresses'