from dataclasses import fields
from django import forms

from .models import Contact, Suscribers


class SuscribersForms(forms.ModelForm):
    class Meta:
        model = Suscribers
        fields = ('email',)
        widgets = {
            'email': forms.EmailInput(
                attrs={
                    'placeholder': 'Correo electrónico...'
                }
            )
        }
        
class ContactForms(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('__all__')
