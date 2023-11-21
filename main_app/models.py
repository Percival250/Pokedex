from django.db import models

class PokeModel(models.Model):
    TYPE = (
        ('Normal', 'Normal'),
        ('Fire', 'Fire'),
        ('Water', 'Water'),
        ('Electric', 'Electric'),
        ('Grass', 'Grass'),
        ('Ice', 'Ice'),
        ('Fighting', 'Fighting'),
        ('Poison', 'Poison'),
        ('Ground', 'Ground'),
        ('Flying', 'Flying'),
        ('Psychic', 'Psychic'),
        ('Bug', 'Bug'),
        ('Rock', 'Rock'),
        ('Ghost', 'Ghost'),
        ('Dragon', 'Dragon'),
        ('Dark', 'Dark'),
        ('Steel', 'Steel'),
        ('Fairy', 'Fairy'),
    )
    SECOND_TYPE = (
        ('None', 'None'),
        ('Normal', 'Normal'),
        ('Fire', 'Fire'),
        ('Water', 'Water'),
        ('Electric', 'Electric'),
        ('Grass', 'Grass'),
        ('Ice', 'Ice'),
        ('Fighting', 'Fighting'),
        ('Poison', 'Poison'),
        ('Ground', 'Ground'),
        ('Flying', 'Flying'),
        ('Psychic', 'Psychic'),
        ('Bug', 'Bug'),
        ('Rock', 'Rock'),
        ('Ghost', 'Ghost'),
        ('Dragon', 'Dragon'),
        ('Dark', 'Dark'),
        ('Steel', 'Steel'),
        ('Fairy', 'Fairy'),
    )
    name = models.CharField(max_length=100, verbose_name='Укажите название покемона')
    region = models.CharField(max_length=100, verbose_name='Укажите название региона')
    image = models.ImageField(max_length=100, upload_to='pokemons/')
    type = models.CharField(max_length=100, choices=TYPE)
    second_type = models.CharField(null=True, max_length=100, choices=SECOND_TYPE)
    number = models.PositiveIntegerField(verbose_name='Укажите номер покемона')
    description = models.TextField(verbose_name='Укажите описание', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name}-{self.region}'

class Slider(models.Model):
    slider = models.URLField()

    def __str__(self):
        return self.slider