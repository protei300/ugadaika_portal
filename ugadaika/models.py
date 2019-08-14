from django.db import models
from django.contrib import admin
# Create your models here.


class CardShirts(models.Model):
    index = models.AutoField(primary_key=True)
    shirt_name = models.CharField(max_length=50, null=False, db_column='Имя рубашки')
    shirt_picture = models.ImageField(upload_to='ugadaika/shirt/', null=False, db_column='Картинка рубашки')

class SoundsFeature(models.Model):
    index = models.AutoField(primary_key=True)
    sound_name = models.CharField(max_length=10, null=False, db_column='Название звука')

    class META:
        ordering = ['sound_name']

    def __str__(self):
        return f"{self.sound_name}"

class SoundPlace(models.Model):
    index = models.AutoField(primary_key=True)
    place_name = models.CharField(max_length=30, null=False, db_column='Положение звука')

    def __str__(self):
        return f"{self.place_name}"

    class META:
        ordering = ['place_name']

### Слоговая структура
class SlogFeature(models.Model):
    index = models.AutoField(primary_key=True)
    slog_name = models.CharField(max_length=200, null=False, db_column='Слоги')

    class META:
        ordering = ['slog_struct_name']

    def __str__(self):
        return self.slog_name


class SuffixFeature(models.Model):
    index = models.AutoField(primary_key=True)
    suffix_name = models.CharField(max_length=200, null=False, db_column='Суффикс')

    class META:
        ordering = ['suffix_name']

    def __str__(self):
        return self.suffix_name


class ShapeFeature(models.Model):
    index = models.AutoField(primary_key=True)
    shape_name = models.CharField(max_length=200, null=False, db_column='Форма')

    class META:
        ordering = ['shape_name']

    def __str__(self):
        return self.shape_name


class ColorFeature(models.Model):
    index = models.AutoField(primary_key=True)
    color_name = models.CharField(max_length=200, null=False, db_column='Цвет')

    class META:
        ordering = ['color_name']

    def __str__(self):
        return self.color_name


class Cards(models.Model):
    index = models.AutoField(primary_key=True)
    card = models.ImageField(upload_to='ugadaika/card/', null=False, db_column='Картинка')
    card_name = models.CharField(max_length=50, null=False, db_column='Название картинки')
    sound = models.ManyToManyField(SoundsFeature, through='CardsSoundsPlace', through_fields=('cards','sounds'))
    slog_feature = models.ForeignKey(SlogFeature, on_delete=models.CASCADE)
    suffix_feature = models.ForeignKey(SuffixFeature, on_delete=models.CASCADE)
    shape_feature = models.ForeignKey(ShapeFeature, on_delete=models.CASCADE)
    color_feature = models.ForeignKey(ColorFeature, on_delete=models.CASCADE)

    class META:
        ordering = ['card_name']

    def __str__(self):
        return f"{self.index} {self.card_name}"

    def sound_display(self):
        return ', '.join([a.sound_name for a in self.sound.all()])





class CardsSoundsPlace(models.Model):
    cards = models.ForeignKey(Cards, on_delete=models.CASCADE)
    sounds = models.ForeignKey(SoundsFeature, on_delete=models.CASCADE)
    place = models.ForeignKey(SoundPlace, on_delete=models.CASCADE)

class displacement_inline(admin.TabularInline):
    model = CardsSoundsPlace
    extra = 1


