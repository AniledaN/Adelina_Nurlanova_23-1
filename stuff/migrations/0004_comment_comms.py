# Generated by Django 4.1.5 on 2023-01-04 17:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stuff', '0003_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='comms',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='stuff.stuff'),
        ),
    ]
