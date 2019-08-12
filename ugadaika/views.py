from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

class IndexView(View, LoginRequiredMixin):

    template_name = 'ugadaika/index.html'
    def get(self,request):
        visit_numbers = request.session.get('visit_numbers',0)
        request.session['visit_numbers'] = visit_numbers + 1
        context = {
            'visit_numbers': visit_numbers
        }
        return render(request, self.template_name, context = context)