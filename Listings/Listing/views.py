from django.shortcuts import render, redirect
from .models import Listing
from .forms import ListingForm
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


def listing_create(request):
    form = ListingForm()
    if request.method == 'POST':
        form = ListingForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {
        "form": form
    }
    return render(request, 'listing/create.html', context)

def listing_update(request, pk):
    listing = Listing.objects.get(id=pk)
    form = ListingForm(instance=listing)
    
    if request.method == 'POST':
        form = ListingForm(request.POST, instance=listing, files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {
        "form": form
    }
    return render(request, 'listing/update.html', context)

def listing_delete(request, pk):
    listing = Listing.objects.get(id=pk)
    listing.delete()
    return redirect("/")