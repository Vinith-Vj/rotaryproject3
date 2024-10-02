from django.shortcuts import render
from .models import *

# Create your views here.

def  home(request):

    cover = homeCoverImage.objects.all()
    context ={'cover': cover}
    return render(request, "index.html", context)

def about(request):

    history = History.objects.all().order_by('-start_year')
    context = {
        'history': history
    }

    return render(request, 'about.html', context)


def project(request):
    return render(request, 'project.html')


def gallery(request):
    return render(request, 'gallery.html')


def contact_view(request):
    return render(request, 'contact.html', {})

def joinus(request):
    return render(request, 'joinus.html', {})