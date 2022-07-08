from django.contrib import admin
from .models import Client, Livre, Commande


# Register your models here.
class ClientAdmin(admin.ModelAdmin):
    list_display = ('nom', 'prenom', 'age', 'tel', 'email')


class LivreAdmin(admin.ModelAdmin):
    list_display = ('titre', 'auteur', 'description', 'prix')


class CommandeAdmin(admin.ModelAdmin):
    list_display = ('client', 'livre', 'statut')


admin.site.register(Client, ClientAdmin)
admin.site.register(Livre, LivreAdmin)
admin.site.register(Commande, CommandeAdmin)
