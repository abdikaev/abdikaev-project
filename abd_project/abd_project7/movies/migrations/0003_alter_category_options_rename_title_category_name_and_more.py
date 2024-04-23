from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='duration',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='movie',
            name='producer',
            field=models.CharField(max_length=255),
        ),
    ]
