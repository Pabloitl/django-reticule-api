from django.core.management.base import BaseCommand

from reticules.models import Reticule

RETICULES = [
    {
        "name": "Ingeniería en Sistemas Computacionales",
        "code": "ISIC-2010-224",
    },
    {
        "name": "Ingeniería en Tecnologías de la información y comunicaciones",
        "code": "ITIC-2010-225",
    },
]


class Command(BaseCommand):
    help = "Seed reticules"

    def handle(self, *args, **options):
        for reticule in RETICULES:
            Reticule.objects.get_or_create(**reticule)
