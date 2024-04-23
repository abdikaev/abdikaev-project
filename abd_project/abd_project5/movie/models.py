from django.db import models


class Category(models.Model):
    name = models.CharField(null=False, blank=False, max_length=255)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return f'ID: {self.id} {self.name}'


class Movie(models.Model):
    title = models.CharField(null=False, max_length=255, blank=False)
    description = models.CharField(null=False, max_length=2000, blank=True, default='')
    producer = models.CharField(null=False, max_length=255, blank=False, default='')
    duration = models.IntegerField(null=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)  # ForeignKey relationship to Category model

    model = 'Movie'
    template_name = 'movie_template.html'

    class Meta:
        verbose_name = 'Movie'
        verbose_name_plural = 'Movies'

    def __str__(self):
        return f'ID: {self.id} {self.title}'
