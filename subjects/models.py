from django.db import models

from reticules.models import Reticule


class Subject(models.Model):
    reticule = models.ForeignKey(
        Reticule, on_delete=models.CASCADE, related_name="subjects"
    )

    name = models.CharField(max_length=100)
    code = models.CharField(max_length=20)
    semester = models.PositiveSmallIntegerField()
    theoretical_hours = models.PositiveSmallIntegerField()
    practical_hours = models.PositiveSmallIntegerField()

    @property
    def total_hours(self) -> int:
        return self.theoretical_hours + self.practical_hours
