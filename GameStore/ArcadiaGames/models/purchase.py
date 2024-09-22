from django.db import models
from .users import Users
from .games import Games

class Purchase(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE)  # Relasi ke tabel Users (satu user banyak transaksi)
    game = models.ForeignKey(Games, on_delete=models.CASCADE)  # Relasi ke tabel Games (satu game banyak transaksi)
    purchase_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} bought {self.game.title} on {self.purchase_date}'
