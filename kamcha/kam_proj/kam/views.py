from django.shortcuts import render
from .models import Kam

def index(request):
    projects = Kam.objects.all()
    return render(request, 'kam/index.html', {'projects': projects})
