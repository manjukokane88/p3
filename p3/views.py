from django.http import HttpResponse
from django.shortcuts import render


def sample(request):
    return render(request,'sample.html')

def sample1(request):
    return render(request,'sample1.html')    