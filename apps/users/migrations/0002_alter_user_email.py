# Generated by Django 4.2.4 on 2023-09-03 08:00

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="email",
            field=models.CharField(
                max_length=255, unique=True, verbose_name="Email Address"
            ),
        ),
    ]