# Generated by Django 3.2 on 2021-05-13 19:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dish', '0003_alter_dish_calories'),
        ('order', '0003_additiondish'),
    ]

    operations = [
        migrations.AddField(
            model_name='additiondish',
            name='dish_de',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='addition_dish', to='dish.dish'),
        ),
        migrations.AddField(
            model_name='additiondish',
            name='dish_en',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='addition_dish', to='dish.dish'),
        ),
        migrations.AddField(
            model_name='order',
            name='dish_de',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='dish.dish'),
        ),
        migrations.AddField(
            model_name='order',
            name='dish_en',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='dish.dish'),
        ),
        migrations.AddField(
            model_name='order',
            name='status_de',
            field=models.IntegerField(choices=[(0, 'Accepted'), (1, 'Completed'), (2, 'Canceled'), (3, 'Deleted')], default=0, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='status_en',
            field=models.IntegerField(choices=[(0, 'Accepted'), (1, 'Completed'), (2, 'Canceled'), (3, 'Deleted')], default=0, null=True),
        ),
    ]
