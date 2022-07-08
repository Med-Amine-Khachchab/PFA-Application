from django.shortcuts import render, redirect
from .models import *
from .forms import CommandeForm, ClientForm, LivreForm
from django.http import HttpResponse


# Create your views here.
def index(request):
    # return HttpResponse('Home page Bonjour IWA')
    clients = Client.objects.all()
    commandes = Commande.objects.all()
    tcommandes = commandes.count()
    tcommandes_L = commandes.filter(statut='Livrer').count()
    tcommandes_att = commandes.filter(statut='En cours').count()
    contexte = {'clients': clients,
                'commandes': commandes,
                'tcommandes': tcommandes,
                'tcommandes_L': tcommandes_L,
                'tcommandes_att': tcommandes_att
                }
    return render(request, 'bookStore/index.html', contexte)


def books(request):
    livres = Livre.objects.all()
    contexte = {'livres': livres}
    return render(request, 'bookStore/books.html', contexte)


def profile(request):
    return render(request, 'bookStore/profile.html')


def afficher_client(request, pk):
    client = Client.objects.get(id=pk)
    commandes = client.commande_set.all()
    contexte = {'client': client,
                'commandes': commandes
                }
    return render(request, 'bookStore/client.html', contexte)


def ajoutercommande(request):
    form = CommandeForm()
    if request.method == 'POST':
        form = CommandeForm(request.POST)
        if form.is_valid():
            form.save()
    contexte = {'form': form}
    return render(request, 'bookStore/ajoutercommande.html', contexte)

def modifiercommande(request, pk):
    commande = Commande.objects.get(id=pk)
    form = CommandeForm(instance=commande)
    if request.method == 'POST':
        form = CommandeForm(request.POST, instance=commande)
        if form.is_valid():
            form.save()
    contexte = {'form': form}
    return render(request, 'bookStore/modifierCommande.html', contexte)

def modifierclient(request, pk):
    client = Client.objects.get(id=pk)
    form = ClientForm(instance=client)
    if request.method == 'POST':
        form = ClientForm(request.POST, instance=client)
        if form.is_valid():
            form.save()
    contexte = {'form': form}
    return render(request, 'bookStore/modifierClient.html', contexte)

def ajouterclient(request):
    form = ClientForm()
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form': form}
    return render(request, 'bookStore/ajouterClient.html', context)


def supprimercommande(request,pk):
    commande=Commande.objects.get(id=pk)
    if request.method == 'POST':
        commande.delete()
        return redirect('/')
    context = {'commande': commande}
    return render(request, 'bookstore/supprimer.html', context)

def supprimerclient(request, pk):
    client = Client.objects.get(id=pk)
    if request.method == 'POST':
        client.delete()
        return redirect('/')
    context = {'client': client}
    return render(request, 'bookstore/supprimer.html', context)
def modifierlivre(request, pk):
    livre = Livre.objects.get(id=pk)
    form = LivreForm(instance=livre)
    if request.method == 'POST':
        form = LivreForm(request.POST, instance=livre)
        if form.is_valid():
            form.save()
            return redirect('../books/')
    contexte = {'form': form}
    return render(request, 'bookStore/modifierLivre.html', contexte)


def ajouterlivre(request):
    form = LivreForm()
    if request.method == 'POST':
        form = LivreForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('../books/')
    context = {'form': form}
    return render(request, 'bookStore/ajouterLivre.html', context)

def supprimerlivre(request, pk):
    livre = Livre.objects.get(id=pk)
    if request.method == 'POST':
        livre.delete()
        return redirect('../books/')
    context = {'livre': livre}
    return render(request, 'bookstore/supprimerLivre.html', context)