# Generated by Django 4.1.5 on 2023-01-04 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stuff', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stuff',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
