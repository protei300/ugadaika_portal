from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import CardShirts, Cards, SoundsFeature, SoundPlace, SuffixFeature, ShapeFeature, ColorFeature, SlogFeature

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
        sounds_features = SoundsFeature.objects.all()
        sound_place = SoundPlace.objects.all()
        suffix_feature = SuffixFeature.objects.all()
        shape_feature = ShapeFeature.objects.all()
        color_feature = ColorFeature.objects.all()
        slog_feature = SlogFeature.objects.all()

        context ={
            "sounds_feature": sounds_features,
            "sound_place": sound_place,
            "suffix_feature": suffix_feature,
            "shape_feature": shape_feature,
            "color_feature": color_feature,
            "slog_feature": slog_feature
        }
        return render(request, self.template_name, context=context)