from pyexpat import model
from statistics import mode
from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

ROLES = (
    ('Direction', 'Direction'),
    ('Gérance', 'Gérance'),
    ('Opérateur', 'Opérateur')
    )

class User(AbstractUser):

    first_name = None
    last_name = None

    nom_complet = models.CharField(max_length=125, verbose_name="Votre Nom Complet")
    admin       = models.BooleanField(default=False, blank=True)
    role        = models.CharField(max_length=125, choices=ROLES) 
    valid       = models.BooleanField(default=False, blank=True)


