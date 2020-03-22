from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from .models import Record
# Create your views here.
class RecordUpdate(UpdateView):
    model = Record
    fields = ['artist', 'released']

class RecordDelete(DeleteView):
    model = Record
    success_url = '/records/'


class RecordCreate(CreateView):
    model = Record
    fields = '__all__'

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html' )

def records_index(request):
    records = Record.objects.all()
    return render(request, 'records/index.html', { 'records': records })

def records_detail(request, record_id):
    record = Record.objects.get(id=record_id)
    return render(request, 'records/detail.html', {'record': record})
