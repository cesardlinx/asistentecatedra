from django.db import models


class Nivel(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        db_table = 'niveles'
        verbose_name_plural = "niveles"

    def __str__(self):
        return self.name
