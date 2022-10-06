from django.core.management.base import BaseCommand

from reticules.models import Reticule
from subjects.models import Subject

RETICULES = [
    {
        "code": "ISIC-2010-224",
        "subjects": [
            {
                "name": "Cálculo Diferencial",
                "code": "ACF-0901",
                "semester": 1,
                "theoretical_hours": 3,
                "practical_hours": 2,
            },
            {
                "name": "Fundamentos de Programación",
                "code": "AED-1285",
                "semester": 1,
                "theoretical_hours": 2,
                "practical_hours": 3,
            },
        ],
    },
    {
        "code": "ITIC-2010-225",
        "subjects": [
            {
                "name": "Cálculo Diferencial",
                "code": "ACF-0901",
                "semester": 1,
                "theoretical_hours": 3,
                "practical_hours": 2,
            },
            {
                "name": "Fundamentos de Programación",
                "code": "AED-1285",
                "semester": 1,
                "theoretical_hours": 2,
                "practical_hours": 3,
            },
        ],
    },
]


class Command(BaseCommand):
    help = "Seed reticules"

    def handle(self, *args, **options):
        for reticule_data in RETICULES:
            reticule = Reticule.objects.filter(code=reticule_data["code"]).first()

            if not reticule:
                continue

            for subject in reticule_data["subjects"]:
                Subject.objects.get_or_create(reticule=reticule, **subject)
