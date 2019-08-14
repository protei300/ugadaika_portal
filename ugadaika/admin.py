from django.contrib import admin
from .models import CardShirts, SoundsFeature, Cards, SoundPlace, \
    CardsSoundsPlace, displacement_inline, SuffixFeature, SlogFeature, ShapeFeature, ColorFeature
# Register your models here.


@admin.register(CardShirts)
class ShirtAdmin(admin.ModelAdmin):
    list_display = ('index', 'shirt_name', 'shirt_picture')

@admin.register(SoundsFeature)
class SoundAdmin(admin.ModelAdmin):
    list_display = ('index', 'sound_name')
    inlines = (displacement_inline,)

@admin.register(SuffixFeature)
class SuffixAdmin(admin.ModelAdmin):
    list_display = ('index', 'suffix_name')

@admin.register(SlogFeature)
class SlogAdmin(admin.ModelAdmin):
    list_display = ('index', 'slog_name')

@admin.register(ShapeFeature)
class ShapeAdmin(admin.ModelAdmin):
    list_display = ('index', 'shape_name')

@admin.register(ColorFeature)
class ColorAdmin(admin.ModelAdmin):
    list_display = ('index', 'color_name')


@admin.register(SoundPlace)
class ShirtAdmin(admin.ModelAdmin):
    list_display = ('index', 'place_name')

@admin.register(Cards)
class CardAdmin(admin.ModelAdmin):
    list_display = ('card_name', 'card', 'sound_display', 'slog_feature', 'suffix_feature', 'shape_feature', 'color_feature')
    inlines = (displacement_inline,)

@admin.register(CardsSoundsPlace)
class CardsSoundsAdmin(admin.ModelAdmin):
    list_display =  ('cards', 'sounds')
