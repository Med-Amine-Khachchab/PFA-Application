from django.db import models


# Create your models here.
class Client(models.Model):
    nom = models.CharField(max_length=50, null=True)
    prenom = models.CharField(max_length=50, null=True)
    tel = models.CharField(max_length=50, null=True)
    age = models.IntegerField()
    email = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.nom


class Livre(models.Model):
    CATEGORIE = (
        ('Sciences', 'Sciences'),
        ('Arts', 'Arts'),
        ('Histoire', 'Histoire'),
        ('Informatique', 'Informatique')
    )
    titre = models.CharField(max_length=100, null=True)
    auteur = models.CharField(max_length=50, null=True)
    description = models.TextField()
    prix = models.FloatField(null=True)
    categorie = models.CharField(max_length=200, null=True, choices=CATEGORIE)
    dateEdition = models.DateField(null=True)
    imageLivre = models.CharField(max_length=1000, null=True)

    def __str__(self):
        return self.titre


class Commande(models.Model):
    STATUT = (
        ('En attente', 'En attente'),
        ('Livrer', 'Livrer'),
        ('En cours', 'En cours'),
        ('Hors service', 'Hors service')
    )
    client = models.ForeignKey(Client, null=True, on_delete=models.SET_NULL)
    livre = models.ForeignKey(Livre, null=True, on_delete=models.SET_NULL)
    statut = models.CharField(max_length=200, null=True, choices=STATUT)
    date_commande = models.DateTimeField(auto_now_add=True, null=True)
