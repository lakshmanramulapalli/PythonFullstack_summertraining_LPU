# Generated by Django 5.2.3 on 2025-06-26 05:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('roll_number', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('age', models.PositiveIntegerField()),
                ('address', models.TextField()),
            ],
        ),
    ]
