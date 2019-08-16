from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import CardShirts, Cards, SoundsFeature, SoundPlace, SuffixFeature, ShapeFeature, ColorFeature, SlogFeature
import json

# Create your views here.

class IndexView(View, LoginRequiredMixin):

    template_name = 'ugadaika/index.html'
    def get(self,request):
        first_shirt = CardShirts.objects.first()
        visit_numbers = request.session.get('visit_numbers',0)
        request.session['visit_numbers'] = visit_numbers + 1
        context = {
            'visit_numbers': visit_numbers,
            'pict': first_shirt.shirt_picture
        }
        return render(request, self.template_name, context = context)

class GenerateGameView(View):
    template_name = 'ugadaika/request.html'


    def get(self,request):
        sounds_features = [ SoundsFeature.META.verbose_name_plural,
                            SoundsFeature.objects.all().values_list('sound_name',flat=True)]
        sound_place = [ SoundPlace.META.verbose_name_plural,
                        SoundPlace.objects.all().values_list('place_name', flat=True)]
        suffix_feature = [ SuffixFeature.META.verbose_name_plural,
                           SuffixFeature.objects.all().values_list('suffix_name', flat=True)]
        shape_feature = [   ShapeFeature.META.verbose_name_plural,
                            ShapeFeature.objects.all().values_list('shape_name', flat=True)]
        color_feature = [   ColorFeature.META.verbose_name_plural,
                            ColorFeature.objects.all().values_list('color_name', flat=True)]
        slog_feature = [    SlogFeature.META.verbose_name_plural,
                            SlogFeature.objects.all().values_list('slog_name', flat=True)]
        items = [sound_place, sounds_features, suffix_feature,
                 shape_feature, color_feature, slog_feature]
        context = {'feature_items': ['hi', 'low'],
                   'features_list': items,
                   }

        return render(request, self.template_name, context=context)