from django import forms
from .models import Enseignant, Salle, Materiel, Emprunt, Accessoire, \
    MaterielAccessoire, EmpruntAccessoire


class EnseignantForm(forms.ModelForm):
    class Meta:
        model = Enseignant
        fields = ['nom', 'prenom']


class SalleForm(forms.ModelForm):
    class Meta:
        model = Salle
        fields = ['nom', 'etage']


class MaterielForm(forms.ModelForm):
    class Meta:
        model = Materiel
        fields = ['nom', 'responsable', 'acheteur', 'budget', 'salle']


class EmpruntForm(forms.ModelForm):
    lieu = forms.ModelChoiceField(
        queryset=Salle.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    class Meta:
        model = Emprunt
        fields = ['materiel', 'possesseur', 'lieu', 'objectif_utilisation']
        widgets = {
            'materiel': forms.Select(attrs={'class': 'form-control'}),
            'possesseur': forms.Select(attrs={'class': 'form-control'}),
        }


class AccessoireForm(forms.ModelForm):
    class Meta:
        model = Accessoire
        fields = ['nom', 'materiel', 'etat']
        widgets = {
            'materiel': forms.Select(attrs={'class': 'form-control'}),
            'etat': forms.Select(attrs={'class': 'form-control'}),
        }


class MaterielAccessoireForm(forms.ModelForm):
    class Meta:
        model = MaterielAccessoire
        fields = ['materiel', 'accessoire']


class EmpruntAccessoireForm(forms.ModelForm):
    class Meta:
        model = EmpruntAccessoire
        fields = ['emprunt', 'accessoire', 'present']
