from django.db import models

# Create your models here.
class OptionSupplementaire(models.Model):
    libelle = models.CharField(db_column='libelle', max_length = 60)

class Demenagement(models.Model):
    relocation_date = models.DateTimeField('date')
    commentaire = models.CharField(db_column='commentaire', max_length = 200)
    volume = models.FloatField(db_column='volume')
    option_supplementaires = models.ManyToManyField(OptionSupplementaire, through='DemenagementOptionsSupplementaire')

class DemenagementOptionsSupplementaire(models.Model):
    demenagement = models.ForeignKey(Demenagement, db_column='demenagement_id', on_delete=models.CASCADE)
    option_supplementaire = models.ForeignKey(OptionSupplementaire, db_column='option_supplementaire_id', on_delete=models.CASCADE)

class TypeAdresse(models.Model):
    libelle = models.CharField(db_column='libelle', max_length = 60)

class Adresse(models.Model):
    rue = models.CharField(db_column='rue', max_length = 200)
    cp = models.CharField(db_column='cp', max_length = 10)
    ville = models.CharField(db_column='ville', max_length = 100)
    pays = models.CharField(db_column='pays', max_length = 100)
    demenagement = models.ForeignKey(Demenagement, db_column='demenagement_id', on_delete=models.CASCADE)
    type_adresse = models.ForeignKey(TypeAdresse, db_column='type_adresse_id', on_delete=models.PROTECT)
