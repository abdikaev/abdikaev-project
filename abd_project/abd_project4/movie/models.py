from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=3000)
    producer = models.CharField(max_length=255)
    duration = models.IntegerField()
    rating = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)

    class Meta:
        verbose_name = 'Movie'
        verbose_name_plural = 'Movies'

    def __str__(self):
        return f'{self.title} (ID: {self.id})'

class BasketItem(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    # Другие поля вашей модели BasketItem

    class Meta:
        verbose_name = 'Basket Item'
        verbose_name_plural = 'Basket Items'
