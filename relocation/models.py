from django.db import models

# Create your models here.
class Relocation(models.Model):
    relocation_date = models.DateTimeField('relocation_date')
    comment = models.CharField(max_length = 200)
    volume = models.FloatField('volume')