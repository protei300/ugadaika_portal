from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
import datetime
from .models import SoundsFeature,SoundPlace, ShapeFeature, ColorFeature, \
    SlogFeature, SuffixFeature, MaterialFeature, SexFeature, EndingFeature

class GetPictures(forms.Form):
    sound_feature_start = forms.ModelMultipleChoiceField(label="Звук в начале", help_text='Выберите звук',
                                         queryset=SoundsFeature.objects.all(), required=False)
    sound_feature_start.group = 1
    sound_feature_middle = forms.ModelMultipleChoiceField(label="Звук в середине", help_text='Выберите звук',
                                                   queryset=SoundsFeature.objects.all(), required=False, )
    sound_feature_middle.group = 1
    sound_feature_end = forms.ModelMultipleChoiceField(label="Звук в конце", help_text='Выберите звук',
                                                   queryset=SoundsFeature.objects.all(), required=False, )

    sound_feature_end.group = 1

    shape_feature = forms.ModelChoiceField(label="Форма", help_text="Выберите форму", required=False,
                                           queryset=ShapeFeature.objects.all())
    shape_feature.group = 2
    color_feature = forms.ModelChoiceField(label="Цвет", help_text="Выберите цвет", required=False,
                                           queryset=ColorFeature.objects.all())
    color_feature.group = 2
    slog_feature = forms.ModelChoiceField(label="Слог", help_text="выберите слог", required=False,
                                           queryset=SlogFeature.objects.all())
    slog_feature.group = 2
    suffix_feature = forms.ModelChoiceField(label="Суффикс", help_text="выберите суффикс", required=False,
                                           queryset=SuffixFeature.objects.all())
    suffix_feature.group = 2
    ending_feature = forms.ModelChoiceField(label="Окончание", help_text="выберите окончание", required=False,
                                            queryset=EndingFeature.objects.all())
    ending_feature.group = 2
    sex_feature = forms.ModelChoiceField(label="Род", help_text="выберите род", required=False,
                                            queryset=SexFeature.objects.all())
    sex_feature.group = 2
    material_feature = forms.ModelChoiceField(label="Материал", help_text="выберите материал", required=False,
                                            queryset=MaterialFeature.objects.all())
    material_feature.group = 2