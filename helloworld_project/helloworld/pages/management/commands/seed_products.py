from django.core.management.base import BaseCommand
from pages.factories import ProductFactory

class Command(BaseCommand):
    help = 'Llena la base de datos con productos'

    def handle(self, *args, **kwargs):
        ProductFactory.create_batch(8)
        self.stdout.write(self.style.SUCCESS('Productos insertados exitosamente'))