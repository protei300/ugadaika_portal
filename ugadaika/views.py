from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import CardShirts, Cards, SoundsFeature, SoundPlace, SuffixFeature, ShapeFeature, ColorFeature, SlogFeature
import json
from .forms import GetPictures

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