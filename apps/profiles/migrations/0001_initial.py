# Generated by Django 4.2.6 on 2023-10-28 15:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Expense',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('expense', models.CharField(max_length=100)),
                ('amount', models.IntegerField()),
                ('category', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Goals',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('goals', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=10000)),
                ('target', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Income',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('income', models.CharField(max_length=100)),
                ('source', models.CharField(max_length=100)),
                ('amount', models.IntegerField()),
                ('frequency', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Profiles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Savings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('savings', models.CharField(max_length=100)),
                ('amount', models.IntegerField()),
                ('type', models.CharField(max_length=100)),
                ('profile', models.ForeignKey(default=list, on_delete=django.db.models.deletion.PROTECT, to='profiles.profiles')),
            ],
        ),
    ]
