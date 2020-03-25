from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from .models import Record, Distributor
from .forms import ListeningForm
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
    not_avail = Distributor.objects.exclude(id__in = record.distributors.all().values_list('id'))
    listening_form = ListeningForm()
    return render(request, 'records/detail.html', {
        'record': record,
        'listening_form': listening_form,
        'distributors': not_avail
    })

def add_listening(request, record_id):
    form = ListeningForm(request.POST)
    if form.is_valid():
        new_listening = form.save(commit=False)
        new_listening.record_id = record_id
        new_listening.save()
    return redirect('detail', record_id=record_id)

def assoc_dist(request, record_id, distributor_id):
  Record.objects.get(id=record_id).distributors.add(distributor_id)
  return redirect('detail', record_id=record_id)

def unassoc_dist(request, record_id, distributor_id):
  Record.objects.get(id=record_id).distributors.remove(distributor_id)
  return redirect('detail', record_id=record_id)

class DistributorList(ListView):
  model = Distributor

class DistributorDetail(DetailView):
  model = Distributor

class DistributorCreate(CreateView):
  model = Distributor
  fields = '__all__'

class DistributorUpdate(UpdateView):
  model = Distributor
  fields = '__all__'

class DistributorDelete(DeleteView):
  model = Distributor
  success_url = '/distributors/'