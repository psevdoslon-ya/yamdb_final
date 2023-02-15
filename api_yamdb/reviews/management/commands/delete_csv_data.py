from django.core.management import BaseCommand
from reviews.models import (Category, Comment, Genre, GenreTitle, Review,
                            Title, User)

MODELS = [User, Review, Comment, Category, Genre, Title, GenreTitle]


class Command(BaseCommand):
    help = 'Комманда для удаления данных из БД.'

    def handle(self, *args, **options):
        print('Удаление данных...')
        for model in MODELS:
            model.objects.all().delete()
