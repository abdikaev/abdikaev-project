from django.db import models


class Movie(models.Model):
    title = models.CharField(null=False, max_length=255, blank=False)
    description = models.CharField(null=False, max_length=2000, blank=True, default='')
    duration = models.PositiveIntegerField(null=False)
    producer = models.CharField(null=False, max_length=255)
    created_at = models.DateTimeField(auto_now=True, null=False)

    class Meta:
        verbose_name = 'Movie'
        verbose_name_plural = 'Movies'

    def __str__(self):
        return f'ID: {self.id} {self.title}'
