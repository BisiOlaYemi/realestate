from django.shortcuts import render
from .models import Listing
# Create your views here.

# CRUD - Create, Retrieve, Update, Delete & list


def listing_list(request):
    listings = Listing.objects.all()
    context = {
        "listings": listings
    }
    return render(request, "listings.html", context)
