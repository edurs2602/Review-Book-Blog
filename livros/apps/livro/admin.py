from django.contrib import admin
from .models import Livro, File
from .functions import read_file


class FileAdmin(admin.ModelAdmin):
    list_display = ['file']  # Lista com os campos que você quer exibir no admin

    # Define a admin action
    def read_excel_action(self, request, queryset):
        # Para cada objeto selecionado no queryset
        for file_instance in queryset:
            # Obtenha o caminho do arquivo
            file_path = file_instance.file.path

            # Chame sua função de leitura de arquivo
            read_file()

        # Exibir uma mensagem de sucesso ao final
        self.message_user(request, "Arquivo(s) lido(s) com sucesso!")

    # Registre a admin action
    actions = [read_excel_action]


admin.site.register(Livro)
admin.site.register(File, FileAdmin)
