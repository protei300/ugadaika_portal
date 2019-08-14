from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import CardShirts

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