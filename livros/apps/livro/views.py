from django.shortcuts import render, get_object_or_404
from .models import Livro


def index(request):
    livros = Livro.objects.all()
    context = {'livros': livros}
    return render(request, 'index.html', context)


def livro(request, livro_id):
    livro_selecionado = get_object_or_404(Livro, pk=livro_id)
    context = {'livro': livro_selecionado}
    return render(request, 'book.html', context)
