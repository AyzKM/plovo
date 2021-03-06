# Generated by Django 3.2 on 2021-05-10 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dish', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='dish',
            name='calories',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='dish',
            name='is_available',
            field=models.BooleanField(default=True),
        ),
    ]
