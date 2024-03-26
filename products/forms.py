from django import forms
from django_summernote.widgets import SummernoteWidget
from .widgets import CustomClearableFileInput
from .models import Product


# Create your forms here.
class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

    image = forms.ImageField(label='Image', required=False, widget=CustomClearableFileInput)
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['description'].widget = SummernoteWidget()
