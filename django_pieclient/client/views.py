from django.shortcuts import render

def home(request):
    return render(request, 'client/home.html')

def about(request):
    return render(request, 'client/about.html')
