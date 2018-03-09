from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.urls import reverse

from .models import Perfil

def index(request):
	perfil = get_list_or_404(Perfil)

	return render(request, 'perfil/index.html', { 'perfis':perfil })

def exibir(request, pk):
	perfil = get_object_or_404(Perfil, pk=pk)

	return render(request, 'perfil/perfil.html', { 'perfil':perfil })