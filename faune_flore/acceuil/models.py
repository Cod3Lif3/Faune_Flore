from django.conf import settings
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.




class Molecule(models.Model):
    InChIKey = models.CharField(max_length=10000)
    moleculeName = models.CharField(max_length=10000,primary_key = True)
    moleculeFormula = models.CharField(max_length=1000)
    crcNumber = models.CharField(max_length=10)
    speciesName = models.CharField(max_length=10000)
    molFileName = models.SlugField(max_length = 100)
    accurateMass = models.CharField(max_length = 100, blank = True)
    casNumber = models.SlugField(max_length = 100)
    compoundType = models.CharField(max_length = 1000,blank=True)
    opticalRotation =  models.CharField(max_length = 100, blank=True)
    publishedDate = models.DateTimeField( default=timezone.now)

    def __str__(self):
        return self.moleculeName