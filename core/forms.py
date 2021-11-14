from django import forms
from .models import Categoria


class CotegoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = '__all__'