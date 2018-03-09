from django.shortcuts import render, get_object_or_404

from .models import Perfil

def index(request):
	return render(request, 'index.html')

def exibir(request, pk):
	perfil = get_object_or_404(Perfil, pk=pk)

	return render(request, 'perfil.html', { 'perfil':perfil })