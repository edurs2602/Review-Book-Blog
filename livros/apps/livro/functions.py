import pandas as pd
import os
from .models import Livro


def read_file():
    path = 'apps/livro/planilha/'
    files = os.listdir(path)

    excel_files = [f for f in files if f.endswith('.xlsx')]

    if excel_files:
        excel_files.sort(key=lambda x: os.path.getmtime(os.path.join(path, x)), reverse=True)

        latest_file = os.path.join(path, excel_files[0])

        df = pd.read_excel(latest_file)

        for index, row in df.iterrows():
            isbn_value = row['ISBN']  # Assumindo que a coluna ISBN está no DataFrame

            # print(row[0])

            # Verificar se o ISBN já existe no banco de dados
            if Livro.objects.filter(isbn=isbn_value).exists():
                # Pular a linha se o ISBN já existir
                print(f"Pular linha {index}: ISBN {isbn_value} já existe.")
                continue

            # Se o ISBN não existe, crie uma nova instância do modelo
            model_instance = Livro(
                obra=row['OBRA'],
                autor=row['AUTOR'],
                indice_catalogo=row['ÍNDICE PARA CATÁLOGO'],
                editora=row['EDITORA'],
                edicao=row['EDIÇÃO'],
                publicacao=row['PUBLICAÇÃO'],
                cidade=row['CIDADE'],
                pais_origem=row['PAÍS DE ORIGEM'],
                isbn=isbn_value
                # Continue mapeando os campos do modelo com as colunas do DataFrame
            )

            # Salve a instância no banco de dados
            model_instance.save()
