from django.shortcuts import render, get_object_or_404
from .models import Livro
from .forms import LivroSearchForm
from django.db.models import Q


def index(request):
    livros = Livro.objects.all()
    form = LivroSearchForm(request.GET)

    queryset = None

    if form.is_valid():
        queryset = livros
        query = form.cleaned_data.get('query')
        # Filtrar a lista de livros com base na consulta
        if query:
            queryset = queryset.filter(
                Q(obra__icontains=query) | Q(autor__icontains=query)
            )

            return render(request, 'index.html', {'livros': queryset})

    context = {'livros': livros}
    return render(request, 'index.html', context)


def livro(request, livro_id):
    livro_selecionado = get_object_or_404(Livro, pk=livro_id)
    context = {'livro': livro_selecionado}
    return render(request, 'book.html', context)

