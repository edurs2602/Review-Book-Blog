# Generated by Django 5.0.1 on 2024-05-03 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('livro', '0002_livro_resenha_alter_livro_autor_alter_livro_cidade_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='apps/livro/planilha', verbose_name='file')),
            ],
        ),
    ]