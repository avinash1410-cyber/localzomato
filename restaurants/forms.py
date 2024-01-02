from django import forms
from .models import Restaurants

class RestaurantsForm(forms.ModelForm):
    class Meta:
        model = Restaurants
        fields = ['name', 'location', 'category']
        # Add any additional fields you want to include in the form

    # You can add custom validation methods or override form behavior here if needed
        
    def clean_name(self):
        name = self.cleaned_data.get('name')
        if len(name) < 3:
            raise forms.ValidationError("Name must be at least 3 characters long.")
        return name