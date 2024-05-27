from django.db import models

class Enseignant(models.Model):
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return f"{self.prenom} {self.nom}"

class Salle(models.Model):
    nom = models.CharField(max_length=50)
    etage = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.nom} (Étage {self.etage})"
class Materiel(models.Model):
    nom = models.CharField(max_length=100)
    responsable = models.ForeignKey(Enseignant, on_delete=models.CASCADE, related_name="materiels_responsable")
    acheteur = models.ForeignKey(Enseignant, on_delete=models.CASCADE, related_name="materiels_achetes", null=True, blank=True)
    budget = models.CharField(max_length=50, choices=[
        ('Annuel', 'Budget Annuel'),
        ('Projet', 'Budget Projet'),
        ('Financement', 'Financement exceptionnel'),
    ], default='Annuel')
    salle = models.ForeignKey(Salle, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.nom

class Accessoire(models.Model):
    nom = models.CharField(max_length=100)
    materiel = models.ForeignKey(Materiel, on_delete=models.CASCADE, null=True, blank=True)
    etat = models.CharField(max_length=50, choices=[
        ('TA', 'Très abîmé'),
        ('A', 'Abîmé'),
        ('BE', 'Bon état'),
        ('N', 'Neuf'),
    ], default='N')

    def __str__(self):
        return self.nom

class MaterielAccessoire(models.Model):
    materiel = models.ForeignKey(Materiel, on_delete=models.CASCADE)
    accessoire = models.ForeignKey(Accessoire, on_delete=models.CASCADE)


class Emprunt(models.Model):
    materiel = models.ForeignKey(Materiel, on_delete=models.CASCADE)
    possesseur = models.ForeignKey(Enseignant, on_delete=models.CASCADE)
    date_emprunt = models.DateTimeField(auto_now_add=True)
    date_retour = models.DateTimeField(null=True, blank=True)
    lieu = models.CharField(max_length=100)
    objectif_utilisation = models.TextField(default="Cours", null=True)

    def __str__(self):
        return f"{self.materiel} emprunté par {self.possesseur}"

class EmpruntAccessoire(models.Model):
    emprunt = models.ForeignKey(Emprunt, on_delete=models.CASCADE)
    accessoire = models.ForeignKey(Accessoire, on_delete=models.CASCADE)
    present = models.BooleanField()

