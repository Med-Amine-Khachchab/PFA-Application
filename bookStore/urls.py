from django.urls import path

from bookStore import views

urlpatterns = [
    path('', views.index, name='index'),
    path('books/', views.books, name='books'),
    path('profile/', views.profile, name='profile'),
    path('client/<str:pk>', views.afficher_client),
    path('ajoutercommande/', views.ajoutercommande, name='ajoutercommande'),
    path('modifiercommande/<str:pk>', views.modifiercommande, name='modifiercommande'),
    path('ajouterclient/', views.ajouterclient, name='ajouterclient'),
    path('modifierclient/<str:pk>', views.modifierclient, name='modifierclient'),
    path('supprimercommande/<str:pk>', views.supprimercommande, name='supprimercommande'),
    path('supprimerclient/<str:pk>', views.supprimerclient, name='supprimerclient'),
    path('ajouterlivre/', views.ajouterlivre, name='ajouterlivre'),
    path('modifierlivre/<str:pk>', views.modifierlivre, name='modifierlivre'),
    path('supprimerlivre/<str:pk>', views.supprimerlivre, name='supprimerlivre')
]