from django import forms
from django_summernote.widgets import SummernoteWidget
from .widgets import CustomClearableFileInput
from .models import Product, Review


# Create your forms here.
class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

    image = forms.ImageField(label='Image', required=False, widget=CustomClearableFileInput)
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['description'].widget = SummernoteWidget()


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['review_name', 'review_text']

        labels = {
            'review_name': 'Name',
            'review_text': 'Review',
        }
