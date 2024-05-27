from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),

    path('enseignants/', views.liste_enseignants, name='liste_enseignants'),
    path('enseignants/ajouter/', views.ajouter_enseignant, name='ajouter_enseignant'),
    path('enseignants/<int:pk>/modifier/', views.modifier_enseignant, name='modifier_enseignant'),
    path('enseignants/<int:pk>/supprimer/', views.supprimer_enseignant, name='supprimer_enseignant'),

    path('salles/', views.liste_salles, name='liste_salles'),
    path('salles/ajouter/', views.ajouter_salle, name='ajouter_salle'),
    path('salles/<int:pk>/modifier/', views.modifier_salle, name='modifier_salle'),
    path('salles/<int:pk>/supprimer/', views.supprimer_salle, name='supprimer_salle'),
    path('salles/<int:salle_id>/materiels/', views.liste_materiels_par_salle, name='liste_materiels_par_salle'),

    path('materiels/', views.liste_materiels, name='liste_materiels'),
    path('materiels/ajouter/', views.ajouter_materiel, name='ajouter_materiel'),
    path('materiels/<int:pk>/modifier/', views.modifier_materiel, name='modifier_materiel'),
    path('materiels/<int:pk>/supprimer/', views.supprimer_materiel, name='supprimer_materiel'),
    path('materiels/<int:materiel_id>/emprunts/', views.liste_emprunts_par_materiel, name='liste_emprunts_par_materiel'),

    path('emprunts/', views.liste_emprunts, name='liste_emprunts'),
    path('emprunts/ajouter/', views.ajouter_emprunt, name='ajouter_emprunt'),
    path('emprunts/<int:pk>/modifier/', views.modifier_emprunt, name='modifier_emprunt'),
    path('emprunts/<int:pk>/supprimer/', views.supprimer_emprunt, name='supprimer_emprunt'),

    path('accessoires/', views.liste_accessoires, name='liste_accessoires'),
    path('accessoires/ajouter/', views.ajouter_accessoire, name='ajouter_accessoire'),
    path('accessoires/<int:pk>/modifier/', views.modifier_accessoire, name='modifier_accessoire'),
    path('accessoires/<int:pk>/supprimer/', views.supprimer_accessoire, name='supprimer_accessoire'),
]
