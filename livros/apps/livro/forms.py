from django import forms


class LivroSearchForm(forms.Form):
    query = forms.CharField(label='Pesquisar por ISBN ou título', max_length=100, required=False)
