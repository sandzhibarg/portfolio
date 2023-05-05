from django.shortcuts import render
from .models import Project

# Create your views here.
def home(request):
    # испортируем все записи о проектах из базы данных в моделях
    projects = Project.objects.all()
    return render(request, 'portfolio/home.html', {'projects': projects})
