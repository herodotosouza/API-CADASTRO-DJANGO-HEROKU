from django import forms
from .models import Fornecedor


class ForncedorForm(forms.ModelForm):
    class Meta:
        model = Fornecedor
        fields = '__all__'

    #def __init__(self, *args, **kwargs):
    #  super().__init__(self, *args, **kwargs)
    #   self.fields['CNPJ'].widget.attrs.update({'class': 'CNPJ'})
     #  self.fields['cep'].widget.attrs.update({'class': 'cep'})






