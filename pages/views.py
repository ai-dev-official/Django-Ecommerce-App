
from django.urls import reverse_lazy
from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = 'home.html'
   