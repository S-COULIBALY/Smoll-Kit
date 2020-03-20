
from django.forms import inlineformset_factory
from django.forms import *
from django import forms
from .models import *


class DemenagementForm(forms.ModelForm):
    class Meta:
        model = Demenagement
        fields =["volume", "date", "formule", "commentaire"]
        widgets = {
            'volume': TextInput(attrs={'class': 'form-control', 'placeholder': "Volume"}),
            'date': DateInput(attrs={'class': 'form-control', 'placeholder': 'date'}),
            'formule': Select(attrs={'class': 'form-control'}),
            'commentaire': Textarea(attrs={'class': 'form-control', 'size': 10, 'cols': 40, 'rows': 4, 'placeholder': 'Votre commentaire'})
            }

        
class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields =['rue', 'code_postale', 'ville', 'pays', 'etage', 'ascenceur']
        widgets = {
            'rue': TextInput(attrs={'class': 'form-control', 'placeholder': "Rue"}),
            'code_postale': TextInput(attrs={'class': 'form-control', 'placeholder': 'Code Postale'}),
            'ville': TextInput(attrs={'class': 'form-control', 'placeholder': 'Ville'}),
            'pays': TextInput(attrs={'class': 'form-control', 'placeholder': 'pays'}),
            'etage': NumberInput(attrs={'class': 'form-control', 'placeholder': 'Étage'}),
            'ascenceur': Select(attrs={'class': 'form-control', 'label': 'Ascenseur'}),
            }



class OptionSupplementaireForm(forms.ModelForm):
    class Meta:
        model= OptionSupplementaire
        fields= ['option']
        widgets = {
            'option': CheckboxSelectMultiple(attrs={})

            }
