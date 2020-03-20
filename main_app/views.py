from django.shortcuts import render
from django.http import HttpResponse
from .models import Record
# Create your views here.


def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html' )

def records_index(request):
    records = Record.objects.all()
    return render(request, 'records/index.html', { 'records': records })