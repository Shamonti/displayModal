from django.shortcuts import render
from datasetApp.models import Dataset

# Create your views here.
def say_hello(request):
  dataset = Dataset.objects.all()
  print('MyOutput', dataset)
  return render(request, 'index.html', {'dataset' : dataset})