from django.forms import ModelForm
from .models import Commande, Client, Livre


class CommandeForm(ModelForm):
    class Meta:
        model = Commande
        fields = '__all__'


class ClientForm(ModelForm):
    class Meta:
        model = Client
        fields = '__all__'
class LivreForm(ModelForm):
    class Meta:
        model = Livre
        fields = '__all__'