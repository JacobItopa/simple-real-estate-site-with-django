from django.shortcuts import render
from .models import Listing
#from django.views import generic

# Create your views here.

def listing_list(request):
    listings=Listing.objects.all()
    context = {
        'listings':listings
    }
    return render(request, 'listing/listings.html', context)

def listing_retrive(request, pk):
    listing = Listing.objects.get(id=pk)
    context = {
        'listing':listing
    }
    return render(request, 'listing/retrieve.html', context)
