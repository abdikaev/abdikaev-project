# Generated by Django 5.0.3 on 2024-04-19 20:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=255)),
                ('description', models.CharField(default='', max_length=3000)),
                ('producer', models.CharField(default='', max_length=255)),
                ('duration', models.IntegerField(default=0)),
            ],
            options={
                'verbose_name': 'Movie',
                'verbose_name_plural': 'Movies',
            },
        ),
    ]