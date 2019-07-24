from django.db import models
from django.template.defaultfilters import slugify


class Planificacion(models.Model):
    name = models.CharField(max_length=40)
    slug = models.SlugField()
    docentes = models.CharField(max_length=255)
    paralelos = models.CharField(max_length=20)
    aprobado_por = models.CharField(max_length=50, blank=True, null=True)
    revisado_por = models.CharField(max_length=50, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)
    observaciones = models.TextField(max_length=200, blank=True, null=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)
