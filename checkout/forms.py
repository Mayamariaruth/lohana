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
        super().__init__(*args, **kwargs)
        placeholders = {
            'full_name': 'Full Name',
            'email': 'Email Address',
            'phone_number': 'Phone Number',
            'postcode': 'Postal Code',
            'town_or_city': 'Town or City',
            'street_address1': 'Street Address 1',
            'street_address2': 'Street Address 2',
            'county': 'County / State',
        }

        self.fields['full_name'].widget.attrs['autofocus'] = True
        
        for field_name, field in self.fields.items():
            if field_name != 'country': 
                if field.required:
                    placeholder = f'{placeholders[field_name]} *'
                else:
                    placeholder = placeholders[field_name]
                field.widget.attrs['placeholder'] = placeholder
            field.widget.attrs['class'] = 'stripe-style-input'
            field.label = False
