from django import forms
from .models import ChildProduct

class ChildProductForm(forms.ModelForm):
    class Meta:
        model = ChildProduct
        fields = '__all__'
        widgets = {
                   'color': forms.TextInput(attrs={'type': 'color'}),
                   }
