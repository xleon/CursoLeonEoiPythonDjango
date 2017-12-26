from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView
from rest_framework import viewsets
from .serializers import *
from .models import *


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        return {'fighters': Fighter.objects.all()}

# def index(request):
#    return HttpResponse('<b>Hola</b> carabola')


class FighterViewSet(viewsets.ModelViewSet):
    queryset = Fighter.objects.all()
    serializer_class = FighterSerializer


class TournamentViewSet(viewsets.ModelViewSet):
    queryset = Tournament.objects.all()
    serializer_class = TournamentSerializer


class CombatViewSet(viewsets.ModelViewSet):
    queryset = Combat.objects.all()
    serializer_class = CombatSerializer
