from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

class Finch: 
    def __init__(self, breed, color, length, region):
        self.breed = breed
        self.color = color
        self.length = length
        self.region = region

finches = [
    Finch('House Finch', 'Rose', 5.5, 'North America'),
    Finch('European Goldfinch', 'Gold and red', 6.0, 'Europe'),

]

def home(request):
    return HttpResponse('<h1>Hello Finch Collectors!</h1>')

def about(request):
    return render(request, 'about.html' )

def finches_index(request):
    return render(request, 'finches/index.html', { 'finches': finches })