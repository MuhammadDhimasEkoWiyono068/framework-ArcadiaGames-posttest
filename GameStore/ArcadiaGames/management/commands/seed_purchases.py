from django.core.management.base import BaseCommand
from random import choice
from ArcadiaGames.models import Users, Games, Purchase

class Command(BaseCommand):
    help = 'Seed purchases'

    def add_arguments(self, parser):
        parser.add_argument('--number', type=int, default=20, help='Number of purchases to create')

    def handle(self, *args, **kwargs):
        number = kwargs['number']
        users = Users.objects.all()
        games = Games.objects.all()

        if not users.exists() or not games.exists():
            self.stdout.write(self.style.ERROR("Please seed Users and Games first!"))
            return

        for _ in range(number):
            purchase = Purchase(
                user=choice(users),
                game=choice(games),
            )
            purchase.save()
            self.stdout.write(self.style.SUCCESS(f'Created purchase for user: {purchase.user.username} on game: {purchase.game.title}'))
