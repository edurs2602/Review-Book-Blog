from django.db import models

from django.db.models.signals import post_save
from django.dispatch import receiver


class Livro(models.Model):

    # def get_path(instance, filename):
    #     extension = filename.split('.')[-1]
    #     uuid = str(instance.obra)
    #     upload_to = f'apps/livro/fotos/{uuid}-foto.{extension}'
    #     return upload_to

    obra = models.CharField(max_length=100, blank=False, null=False, verbose_name='Obra');
    autor = models.CharField(max_length=100, verbose_name='Autor');
    indice_catalogo = models.CharField(max_length=100, verbose_name='Indice Para Catalogo');
    editora = models.CharField(max_length=100, verbose_name='Editora');
    edicao = models.CharField(max_length=12, verbose_name='Edição');
    publicacao = models.IntegerField(verbose_name='Publicação');
    cidade = models.CharField(max_length=50, verbose_name='Cidade');
    pais_origem = models.CharField(max_length=50, verbose_name='Pais de Origem');
    isbn = models.CharField(max_length=40, verbose_name='ISBN');
    resenha = models.TextField(blank=True, null=True, verbose_name='Resenha');

    # foto = models.ImageField(
    #     upload_to=get_path, height_field=None, width_field=None, max_length=100, verbose_name='foto')

    def __str__(self):
        return f'{str(self.obra)} - {self.autor}';


class File(models.Model):
    path = 'apps/livro/planilha'

    file = models.FileField(upload_to=path, verbose_name='file')

    def __str__(self):
        return f'{str(self.file)}';


@receiver(post_save, sender=File)
def delete_old_files(sender, instance, **kwargs):
    old_files = File.objects.exclude(pk=instance.pk)
    for old_file in old_files:
        old_file.file.delete()
        old_file.delete()
