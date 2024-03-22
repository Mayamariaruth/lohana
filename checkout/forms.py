from django import forms
from .models import Order


# Create your forms here.
class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('full_name', 'email', 'phone_number',
                  'street_address1', 'street_address2',
                  'town_or_city', 'postcode', 'country',
                  'county',)

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'full_name': 'Full Name',
            'email': 'Email Address',
            'phone_number': 'Phone Number',
            'country': 'Country',
            'postcode': 'Postal Code',
            'town_or_city': 'Town or City',
            'street_address1': 'Street Address 1',
            'street_address2': 'Street Address 2',
            'county': 'County',
        }

        # Set autofocus on the first field
        self.fields['full_name'].widget.attrs['autofocus'] = True
        
        # Iterate over fields to set placeholders, classes, and remove labels
        for field_name, field in self.fields.items():
            if field.required:
                placeholder = f'{placeholders[field_name]} *'
            else:
                placeholder = placeholders[field_name]
            field.widget.attrs['placeholder'] = placeholder
            field.widget.attrs['class'] = 'stripe-style-input'
            field.label = False