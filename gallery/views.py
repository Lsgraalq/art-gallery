from django.shortcuts import render, get_object_or_404
from .models import Painting

# Create your views here.
def gallery(request):
    paintings = Painting.objects.all()
    return render(request, 'gallery/gallery.html', {"paintings":paintings})

def painting_detail(request, slug):
    painting = get_object_or_404(Painting, slug=slug)
    return render(request, 'gallery/painting.html', {'painting': painting})

def home(request):
    return render(request,'gallery/home.html')

def donation(request):
    return render(request,'gallery/donation.html')