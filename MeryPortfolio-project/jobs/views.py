from django.shortcuts import render

# Create your views here.

def mery(request):
    return render(request, 'jobs/home.html')
