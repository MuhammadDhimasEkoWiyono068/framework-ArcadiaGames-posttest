from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.timezone import now
import os

def game_image_upload_path(instance, filename):
    # Ambil ekstensi file asli (contoh: '.jpg', '.png')
    ext = filename.split('.')[-1]
    # Buat nama file baru berdasarkan judul game dan waktu saat ini
    filename = f"{instance.title}_{now().strftime('%Y%m%d%H%M%S')}.{ext}"
    # Simpan di folder 'games_images/'
    return os.path.join('games_images/', filename)

class Games(models.Model):
    title = models.CharField(max_length=255, unique=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    developer = models.CharField(max_length=255)
    release_date = models.DateField()
    image = models.ImageField(upload_to=game_image_upload_path, default='games_images/default.png')

    def __str__(self):
        return self.title
