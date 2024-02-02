# Generated by Django 5.0.1 on 2024-02-01 08:09

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking_app', '0002_alter_room_category'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_number', models.IntegerField()),
                ('check_in_date', models.DateTimeField(auto_now_add=True)),
                ('check_out_date', models.DateTimeField(auto_now_add=True)),
                ('total_cost', models.DecimalField(decimal_places=1, max_digits=12)),
                ('room_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='booking_app.room')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=1, max_digits=12)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('pay_method', models.CharField(max_length=50)),
                ('booking_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='booking_app.booking')),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review', models.TextField()),
                ('rating', models.IntegerField()),
                ('review_date', models.DateTimeField(auto_now_add=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
