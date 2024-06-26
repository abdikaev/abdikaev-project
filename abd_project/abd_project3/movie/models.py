from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=3000)
    producer = models.CharField(max_length=255)
    duration = models.IntegerField()

    class Meta:
        verbose_name = 'Movie'
        verbose_name_plural = 'Movies'

    def __str__(self):
        return f'{self.title} (ID: {self.id})'
