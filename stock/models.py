from django.db import models
import uuid
from users.models import User


CLASSI = (
        ('Superette', 'Superette'),
        ('Global', 'Global'),
        ('Stock', 'Stock'),
        ('Fruit et Légumes', 'Fruit et Légumes'),
        ('Viandes et Volailles', 'Viandes et Volailles'),
        ('Poissons', 'Poissons'),
        ('Epices', 'Epices'),
        ('Boissons Chaudes', 'Boissons Chaudes'),
        ('Boissons Fraiches', 'Boissons Fraiches'),
        ('Pains', 'Pains'),
        ('Epiceries et Conserves', 'Epiceries et Conserves'),
        ('Huiles et Vinaigres', 'Huiles et Vinaigres'),
        ('Consomables cuisines', 'Consomables cuisines'),
        ('Fournitures cafe et resto', 'Fournitures cafe et resto'),
        ('Produits et Patisseries', 'Produits et Patisseries'),
        ('BOF', 'BOF'),
        ('Produits Ménage', 'Produits Ménage'),
        ('Frait transport', 'Frait transport'),
        ('Fourniture Bureau', 'Fourniture Bureau'),
        ('Divers', 'Divers'),
        )

POSTE = (
    ('CAFE', 'CAFE'),
    ('RESTAURENT', 'RESTAURENT'),
    ('LAITERIE', 'LAITERIE'),
    ('GRILLADE', 'GRILLADE'),
    ('TAFERNOUTE', 'TAFERNOUTE'),
    ('SNACK', 'SNACK'),
    ('Superette', 'Superette')
    )


class Fournisseur(models.Model):
    nom = models.CharField(max_length=125, verbose_name="Nom du fournisseurs")
    adresse = models.CharField(max_length=125, verbose_name="Adresse du fournissuer")
    tel = models.CharField(max_length=125, verbose_name="Numéro de télephone")

    def __str__(self):
        return self.nom


class Article(models.Model):
    uid = models.UUIDField(default=uuid.uuid1, editable=False)
    nom = models.CharField(max_length=125, verbose_name="Nom de l'article")
    group = models.CharField(max_length=125, choices=CLASSI , verbose_name="Classification")
    fourni      = models.ForeignKey(Fournisseur, on_delete=models.CASCADE, verbose_name="Fournisseur")
    qte  = models.DecimalField(max_digits=12, decimal_places=2, blank=True, verbose_name="Quantité En Stock")
    single_value = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    prix = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True, verbose_name="Prix Unitaire")
    ref = models.CharField(max_length=125, blank=True)

    def save(self, *args, **kwargs): 
        suffix = f"{self.uid}"
        print(self.uid)
        pref   = "ART"
        self.ref = f"{pref}-{suffix}"[0:10]
        super(Article, self).save(*args, **kwargs)

    def __str__(self):
        return self.nom

class Taking(models.Model):
    uid = models.UUIDField(default=uuid.uuid1, editable=False)
    user      = models.ForeignKey(User, on_delete=models.CASCADE,  null=True)
    poste = models.CharField(max_length=125, blank=True, choices=POSTE, null=True, verbose_name="Prélévement pour quel Poste ?")
    made_on  = models.DateTimeField(auto_now=True, verbose_name="Date et heure de sortie")
    total_value = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    ref       = models.CharField(max_length=125, blank=True, verbose_name="Référence unique")

    def save(self, *args, **kwargs): 
        suffix = f"{self.uid}"
        print(self.uid)
        pref   = "ART"
        self.ref = f"{pref}-{suffix}"[0:10]
        super(Taking, self).save(*args, **kwargs)
    
    def __str__(self):
        return self.ref

class TakingArticles(models.Model):
    taking   = models.ForeignKey(Taking, on_delete=models.CASCADE, related_name="article_sortant")
    articles = models.ForeignKey(Article, on_delete=models.CASCADE)
    qte      = models.DecimalField(max_digits=12, decimal_places=2)

class Feeding(models.Model):
    uid = models.UUIDField(default=uuid.uuid1, editable=False)
    user      = models.ForeignKey(User, on_delete=models.CASCADE)
    br = models.CharField(max_length=125, verbose_name="Bon de réception N°", null=True)
    fournisseur = models.ForeignKey(Fournisseur, on_delete=models.CASCADE, related_name="taking_fourni", verbose_name="Fournisseur", null=True)
    date_feed =  models.DateTimeField(auto_now_add=True, verbose_name="Fait le")
    total_value = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    
    def __str__(self):
        return str(self.br)

class FeedingArticles(models.Model): 
    feeding   = models.ForeignKey(Feeding, on_delete=models.CASCADE, related_name="article_entrant")
    articles = models.ForeignKey(Article, on_delete=models.CASCADE)
    prix_unitaire = models.DecimalField(max_digits=12, decimal_places=2)
    qte      = models.DecimalField(max_digits=12, decimal_places=2)

    def __str__(self):
        return str(self.qte)










