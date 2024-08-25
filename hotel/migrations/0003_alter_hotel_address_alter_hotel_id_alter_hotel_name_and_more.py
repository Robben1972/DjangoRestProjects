# Generated by Django 5.1 on 2024-08-25 05:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0002_alter_room_price_per_night'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotel',
            name='address',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='hotel',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='hotel',
            name='name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='check_in',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='check_out',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='room',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reservations', to='hotel.room'),
        ),
        migrations.AlterField(
            model_name='room',
            name='hotel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rooms', to='hotel.hotel'),
        ),
        migrations.AlterField(
            model_name='room',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='room',
            name='number',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='room',
            name='price_per_night',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]