from django.db import models


class Area(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        db_table = 'areas'
        verbose_name_plural = "áreas"

    def __str__(self):
        return self.name


