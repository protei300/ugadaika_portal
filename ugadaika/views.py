from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import CardShirts, Cards, SoundsFeature, SoundPlace, SuffixFeature, ShapeFeature, ColorFeature, SlogFeature
import numpy as np
from .forms import GetPictures
from random import shuffle
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

        }
        return render(request, self.template_name, context = context)

class GenerateGameView(View):
    template_name = 'ugadaika/request.html'


    def get(self,request):
        form = GetPictures()


        context = {
                   'form': form,
                   }

        return render(request, self.template_name, context=context)

    def post(self, request):
        form = GetPictures(request.POST)
        context ={}
        if form.is_valid():
            for data in form.cleaned_data:
                print (form.cleaned_data[data])
            context['form'] = form
        return render(request, self.template_name, context=context)


class CardsViewCreated(View):
    template_name = 'ugadaika/cards.html'

    def post(self, request):
        form = GetPictures(request.POST)

        if form.is_valid():
            res=Cards.objects.all()
            if form.cleaned_data['shape_feature'] is not None:
                res = res.filter(shape_feature__shape_name=form.cleaned_data['shape_feature'])
            if form.cleaned_data['color_feature'] is not None:
                res = res.filter(color_feature__color_name=form.cleaned_data['color_feature'])
            if form.cleaned_data['slog_feature'] is not None:
                res = res.filter(slog_feature__slog_name=form.cleaned_data['slog_feature'])
            if form.cleaned_data['suffix_feature'] is not None:
                res = res.filter(suffix_feature__suffix_name=form.cleaned_data['suffix_feature'])
            if form.cleaned_data['ending_feature'] is not None:
                res = res.filter(ending_feature__ending_name=form.cleaned_data['ending_feature'])
            if form.cleaned_data['sex_feature'] is not None:
                res = res.filter(sex_feature__sex_name=form.cleaned_data['sex_feature'])
            if form.cleaned_data['material_feature'] is not None:
                res = res.filter(material_feature__material_name=form.cleaned_data['material_feature'])
            if form.cleaned_data['sound_feature_start'].exists():
                res = res.filter(sound__in = form.cleaned_data['sound_feature_start'],
                                 cardssoundsplace__place__place_name__iexact='начало')
            if form.cleaned_data['sound_feature_middle'].exists():
                res = res.filter(sound__in = form.cleaned_data['sound_feature_middle'],
                                 cardssoundsplace__place__place_name__iexact='середина')
            if form.cleaned_data['sound_feature_end'].exists():
                res = res.filter(sound__in = form.cleaned_data['sound_feature_end'],
                                 cardssoundsplace__place__place_name__iexact='конец')

            card_shirt = CardShirts.objects.first().shirt_picture

        ####### Создаем и наполняем список картинок #########
            res_list = list(res)
            new_res_list = res_list.copy()
            res_list.extend(new_res_list)
            shuffle(res_list)
            print (res_list)
            ser_list = []
            for elem in res_list:
                ser_list.append(elem.card.url)
            json_slzd = json.dumps(ser_list)
            print (json_slzd)


            context = {
                'card_shirt': card_shirt,
                'json_slzd': json_slzd,
            }

            return render(request, self.template_name, context=context)