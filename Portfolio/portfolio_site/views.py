from django.shortcuts import render
from django.views import generic
# Create your views here.
from django.http import HttpResponse
from django.template import loader


class IndexView(generic.ListView):
    template = 'portfolio_site/index.html'
    return HttpResponse(template.render(request))