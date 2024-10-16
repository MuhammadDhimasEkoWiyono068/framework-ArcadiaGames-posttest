from django.shortcuts import render, redirect, get_object_or_404
from .models import Games
from django.contrib.humanize.templatetags.humanize import intcomma
from django.db.models import Q
from .forms import GamesForm
from django.contrib import messages
from django.http import JsonResponse

# Create your views here.
def homepage(request):
    return render(request, 'homepage/index.html')

def about(request):
    return render(request, 'homepage/about.html')

def CRUD_Games(request):
    games = Games.objects.all()  # Mengambil semua data game
    return render(request, 'homepage/CRUD_Games.html', {'games': games})

def CRUD_Games(request):
    query = request.GET.get('q')
    if query:
        games = Games.objects.filter(
            Q(title__icontains=query) |
            Q(description__icontains=query) |
            Q(developer__icontains=query)
        )
    else:
        games = Games.objects.all()
    
    return render(request, 'homepage/CRUD_Games.html', {'games': games, 'query': query})

# Add Game
def add_game(request):
    if request.method == 'POST':
        form = GamesForm(request.POST, request.FILES)  # Tambahkan request.FILES untuk mengupload gambar
        if form.is_valid():
            form.save()  # Simpan data game ke database
            messages.success(request, 'Game berhasil dibuat!')  # Pesan sukses
            return redirect('GameList')  # Redirect ke halaman index game
    else:
        form = GamesForm()
    return render(request, 'games/add_games.html', {'form': form})

# UPDATE Game
def update_game(request, game_id):
    game = get_object_or_404(Games, id=game_id)
    
    if request.method == 'POST':
        form = GamesForm(request.POST, request.FILES, instance=game)  # Tambahkan request.FILES untuk mengupload gambar
        if form.is_valid():
            form.save()  # Simpan perubahan ke database
            messages.success(request, 'Data game berhasil diubah!')
            return redirect('GameList')  # Redirect ke halaman index game
    else:
        form = GamesForm(instance=game)  # Mengisi form dengan data game yang ada
    
    return render(request, 'games/update_game.html', {'form': form, 'game': game})

# DELETE Game
def game_delete(request, game_id):
    if request.method == 'POST':
        game = get_object_or_404(Games, id=game_id)
        game.delete()
        return JsonResponse({'status': 'success'})
    return JsonResponse({'status': 'error'}, status=400)