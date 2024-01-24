from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('book/<int:livro_id>/', views.livro, name='livro'),
]