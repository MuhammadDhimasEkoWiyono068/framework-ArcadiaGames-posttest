from django.contrib import admin
from .models.games import Games
from .models.purchase import Purchase
from .models.users import Users
from random import choice

class GameAdmin(admin.ModelAdmin):
    list_display = ('title', 'developer', 'price', 'release_date')

    def save_model(self, request, obj, form, change):
        # Simpan Game terlebih dahulu
        super().save_model(request, obj, form, change)

        # Buat transaksi otomatis setelah game disimpan
        # Pilih user acak yang ada di database
        users = Users.objects.filter(role=Users.CUSTOMER)
        
        if users.exists():
            random_user = choice(users)  # Pilih user acak
            Purchase.objects.create(user=random_user, game=obj)

            self.message_user(request, f'Purchase otomatis dibuat untuk {random_user.username} pada game {obj.title}')

# Custom admin untuk model Users
class UsersAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'phone_number', 'role')
    list_filter = ('role',)
    search_fields = ('username', 'email')

# Custom admin untuk model Purchase
class PurchaseAdmin(admin.ModelAdmin):
    list_display = ('user', 'game', 'purchase_date')
    list_filter = ('purchase_date',)
    search_fields = ('user__username', 'game__title')

# Daftarkan model Games dengan custom admin
admin.site.register(Games, GameAdmin)
admin.site.register(Users, UsersAdmin)
admin.site.register(Purchase, PurchaseAdmin)
