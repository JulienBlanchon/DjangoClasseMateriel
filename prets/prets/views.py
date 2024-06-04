from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import (Enseignant, Salle, Materiel, Emprunt, Accessoire,
                     MaterielAccessoire, EmpruntAccessoire)
from .forms import (EnseignantForm, SalleForm, MaterielForm, EmpruntForm, AccessoireForm)


# --- Pages de liste ---

def index(request):
    return render(request, 'index.html')


def liste_enseignants(request):
    enseignants = Enseignant.objects.all()
    return render(request, 'liste_enseignants.html', {'enseignants': enseignants})


def liste_salles(request):
    salles = Salle.objects.all()
    return render(request, 'liste_salles.html', {'salles': salles})


def liste_materiels(request):
    materiels = Materiel.objects.all()
    return render(request, 'liste_materiels.html', {'materiels': materiels})


def liste_emprunts(request):
    emprunts = Emprunt.objects.all()
    return render(request, 'liste_emprunts.html', {'emprunts': emprunts})



def liste_accessoires(request):
    accessoires = Accessoire.objects.all()
    return render(request, 'liste_accessoires.html', {'accessoires': accessoires})


def liste_materiels_par_salle(request, salle_id):
    salle = get_object_or_404(Salle, pk=salle_id)
    materiels = Materiel.objects.filter(salle=salle)
    return render(request, 'liste_materiels_par_salle.html', {'salle': salle, 'materiels': materiels})


def liste_emprunts_par_materiel(request, materiel_id):
    materiel = get_object_or_404(Materiel, pk=materiel_id)
    emprunts = Emprunt.objects.filter(materiel=materiel).order_by('-date_emprunt')
    return render(request, 'liste_emprunts_par_materiel.html', {'materiel': materiel, 'emprunts': emprunts})


# --- Pages d'ajout ---

def ajouter_enseignant(request):
    if request.method == 'POST':
        form = EnseignantForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "L'enseignant a été ajouté avec succès.")
            return redirect('liste_enseignants')
    else:
        form = EnseignantForm()
    return render(request, 'ajouter_enseignant.html', {'form': form})


def ajouter_salle(request):
    if request.method == 'POST':
        form = SalleForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "La salle a été ajoutée avec succès.")
            return redirect('liste_salles')
    else:
        form = SalleForm()
    return render(request, 'ajouter_salle.html', {'form': form})


def ajouter_materiel(request):
    if request.method == 'POST':
        form = MaterielForm(request.POST)
        if form.is_valid():
            materiel = form.save()
            accessoire_ids = request.POST.getlist('accessoires')
            for accessoire_id in accessoire_ids:
                MaterielAccessoire.objects.create(materiel=materiel, accessoire_id=accessoire_id)
            messages.success(request, "Le matériel a été ajouté avec succès.")
            return redirect('liste_materiels')
    else:
        form = MaterielForm()
        accessoire = Accessoire.objects.all()
        return render(request, 'ajouter_materiel.html', {'form': form, 'accessoires': accessoire})


def ajouter_emprunt(request):
    if request.method == 'POST':
        form = EmpruntForm(request.POST)
        if form.is_valid():
            emprunt = form.save()
            accessoire_ids = request.POST.getlist('accessoires')
            for accessoire_id in accessoire_ids:
                accessoire = get_object_or_404(Accessoire, pk=accessoire_id)
                EmpruntAccessoire.objects.create(emprunt=emprunt, accessoire=accessoire, present=True)
            messages.success(request, "L'emprunt a été ajouté avec succès.")
            return redirect('liste_emprunts')
    else:
        form = EmpruntForm()
        salles = Salle.objects.all()
        accessoires = Accessoire.objects.all() if not request.GET.get('materiel') else Accessoire.objects.filter(
            materiel=request.GET.get('materiel'))
    return render(request, 'ajouter_emprunt.html', {'form': form, 'accessoires': accessoires, 'salles': salles})


def ajouter_accessoire(request):
    if request.method == 'POST':
        form = AccessoireForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "L'accessoire a été ajouté avec succès.")
            return redirect('liste_accessoires')
    else:
        form = AccessoireForm()
        return render(request, 'ajouter_accessoire.html', {'form': form})


# --- Pages de modification ---

def modifier_enseignant(request, pk):
    enseignant = get_object_or_404(Enseignant, pk=pk)
    if request.method == 'POST':
        form = EnseignantForm(request.POST, instance=enseignant)
        if form.is_valid():
            form.save()
            messages.success(request, "L'enseignant a été modifié avec succès.")
            return redirect('liste_enseignants')
    else:
        form = EnseignantForm(instance=enseignant)
    return render(request, 'modifier_enseignant.html', {'form': form, 'enseignant': enseignant})


def modifier_salle(request, pk):
    salle = get_object_or_404(Salle, pk=pk)
    if request.method == 'POST':
        form = SalleForm(request.POST, instance=salle)
        if form.is_valid():
            form.save()
            messages.success(request, "La salle a été modifiée avec succès.")
            return redirect('liste_salles')
    else:
        form = SalleForm(instance=salle)
    return render(request, 'modifier_salle.html', {'form': form, 'salle': salle})


def modifier_materiel(request, pk):
    materiel = get_object_or_404(Materiel, pk=pk)
    if request.method == 'POST':
        form = MaterielForm(request.POST, instance=materiel)
        if form.is_valid():
            form.save()
            MaterielAccessoire.objects.filter(materiel=materiel).delete()
            accessoire_ids = request.POST.getlist('accessoires')
            for accessoire_id in accessoire_ids:
                MaterielAccessoire.objects.create(materiel=materiel, accessoire_id=accessoire_id)
            messages.success(request, "Le matériel a été modifié avec succès.")
            return redirect('liste_materiels')
    else:
        form = MaterielForm(instance=materiel)
    accessoires = Accessoire.objects.all()
    materiel_accessoires = materiel.materielaccessoire_set.all()
    return render(request, 'modifier_materiel.html', {'form': form, 'materiel': materiel, 'accessoires': accessoires,
                                                      'materiel_accessoires': materiel_accessoires
                                                      })


def modifier_emprunt(request, pk):
    emprunt = get_object_or_404(Emprunt, pk=pk)
    emprunt_accessoires = emprunt.empruntaccessoire_set.all()

    if request.method == 'POST':
        emprunt_form = EmpruntForm(request.POST, instance=emprunt)

        if emprunt_form.is_valid():
            emprunt_form.save()

            # Mettre à jour les accessoires empruntés
            EmpruntAccessoire.objects.filter(emprunt=emprunt).delete()
            accessoire_ids = request.POST.getlist('accessoires')
            etats_accessoires = request.POST.getlist('etat_accessoire')
            for accessoire_id, etat in zip(accessoire_ids, etats_accessoires):
                accessoire = get_object_or_404(Accessoire, pk=accessoire_id)
                EmpruntAccessoire.objects.create(
                    emprunt=emprunt,
                    accessoire=accessoire,
                    present=True,
                    etat=etat
                )

            messages.success(request, "L'emprunt a été modifié avec succès.")
            return redirect('liste_emprunts')

    else:
        emprunt_form = EmpruntForm(instance=emprunt)

    accessoires = Accessoire.objects.filter(materiel=emprunt.materiel)

    # Get initial states for accessories in this emprunt
    initial_accessory_states = {}
    for ea in emprunt_accessoires:
        initial_accessory_states[ea.accessoire.id] = ea.accessoire.etat  # Correction ici

    return render(request, 'modifier_emprunt.html', {
        'form': emprunt_form,
        'emprunt': emprunt,
        'accessoires': accessoires,
        'initial_accessory_states': initial_accessory_states,
    })


def modifier_accessoire(request, pk):
    accessoire = get_object_or_404(Accessoire, pk=pk)
    if request.method == 'POST':
        form = AccessoireForm(request.POST, instance=accessoire)
        if form.is_valid():
            form.save()
            messages.success(request, "L'accessoire a été modifié avec succès.")
            return redirect('liste_accessoires')
    else:
        form = AccessoireForm(instance=accessoire)
    return render(request, 'modifier_accessoire.html', {'form': form, 'accessoire': accessoire})


# --- Pages de suppression ---

def supprimer_enseignant(request, pk):
    enseignant = get_object_or_404(Enseignant, pk=pk)
    if request.method == 'POST':
        enseignant.delete()
        messages.success(request, "L'enseignant a été supprimé avec succès.")
        return redirect('liste_enseignants')
    return render(request, 'supprimer_enseignant.html', {'enseignant': enseignant})


def supprimer_salle(request, pk):
    salle = get_object_or_404(Salle, pk=pk)
    if request.method == 'POST':
        salle.delete()
        messages.success(request, "La salle a été supprimé avec succès.")
        return redirect('liste_salles')
    return render(request, 'supprimer_salle.html', {'salle': salle})


def supprimer_materiel(request, pk):
    materiel = get_object_or_404(Materiel, pk=pk)
    if request.method == 'POST':
        materiel.delete()
        messages.success(request, "Le matériel a été supprimé avec succès.")
        return redirect('liste_materiels')
    return render(request, 'supprimer_materiel.html', {'materiel': materiel})


def supprimer_emprunt(request, pk):
    emprunt = get_object_or_404(Emprunt, pk=pk)
    if request.method == 'POST':
        emprunt.delete()
        messages.success(request, "L'emprunt a été supprimé avec succès.")
        return redirect('liste_emprunts')
    return render(request, 'supprimer_emprunt.html', {'emprunt': emprunt})


def supprimer_accessoire(request, pk):
    accessoire = get_object_or_404(Accessoire, pk=pk)
    if request.method == 'POST':
        accessoire.delete()
        messages.success(request, "L'accessoire a été supprimé avec succès.")
        return redirect('liste_accessoires')
    return render(request, 'supprimer_accessoire.html', {'accessoire': accessoire})
