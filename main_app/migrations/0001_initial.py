# Generated by Django 4.2.7 on 2023-11-21 03:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PokeModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Укажите название покемона')),
                ('region', models.CharField(max_length=100, verbose_name='Укажите название региона')),
                ('image', models.ImageField(upload_to='pokemons/')),
                ('type', models.CharField(choices=[('Normal', 'Normal'), ('Fire', 'Fire'), ('Water', 'Water'), ('Electric', 'Electric'), ('Grass', 'Grass'), ('Ice', 'Ice'), ('Fighting', 'Fighting'), ('Poison', 'Poison'), ('Ground', 'Ground'), ('Flying', 'Flying'), ('Psychic', 'Psychic'), ('Bug', 'Bug'), ('Rock', 'Rock'), ('Ghost', 'Ghost'), ('Dragon', 'Dragon'), ('Dark', 'Dark'), ('Steel', 'Steel'), ('Fairy', 'Fairy')], max_length=100)),
                ('number', models.PositiveIntegerField(verbose_name='Укажите номер покемона')),
                ('description', models.TextField(blank=True, verbose_name='Укажите описание')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Покемон',
                'verbose_name_plural': 'Покемоны',
            },
        ),
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slider', models.URLField()),
            ],
        ),
    ]
