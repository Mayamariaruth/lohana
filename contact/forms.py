from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'user_order', 'subject', 'message']

        labels = {'user_order': 'Order Number'}
        placeholders = {
            'name': 'First & Lastname',
            'email': 'Emailaddress',
            'user_order': 'Order number',
            'subject': 'Subject',
            'message': 'Message'
        }
