from django import forms
from .models import UserProfile


# Create your forms here.
class UserDetailsForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ('user',)

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'user_phone_number': 'Phone Number',
            'user_postcode': 'Postal Code',
            'user_town_or_city': 'Town or City',
            'user_street_address1': 'Street Address 1',
            'user_street_address2': 'Street Address 2',
            'user_county': 'County / State',
        }

        self.fields['user_phone_number'].widget.attrs['autofocus'] = True
        
        for field_name, field in self.fields.items():
            if field_name != 'user_country': 
                if field.required:
                    placeholder = f'{placeholders[field_name]} *'
                else:
                    placeholder = placeholders[field_name]
                field.widget.attrs['placeholder'] = placeholder
            field.widget.attrs['class'] = 'stripe-style-input'
            field.label = False
