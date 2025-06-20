from django.shortcuts import render
from django.views.generic import TemplateView

class Home (TemplateView):
    template_name = 'home.html'

class About (TemplateView):
    template_name = 'about.html'


class Contact (TemplateView):
    template_name = 'contact.html'

class Programmes (TemplateView):
    template_name = 'programme.html'
