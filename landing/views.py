from django.shortcuts import render

# Create your views here.

def landing_view(request):
    template = 'landing/landing.html'
    return render(request, template)
