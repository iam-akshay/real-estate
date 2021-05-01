from django.shortcuts import render, get_object_or_404
from .models import Listing
from django.core.paginator import Paginator

def listings(request):
    listings = Listing.objects.order_by("-list_date").filter(
        is_published = True
    )
    paginator = Paginator(listings, 25)
    current_page = request.GET.get("page", 1)
    paginate_listings = paginator.get_page(current_page)
    context = {
        "listings": paginate_listings
    }
    return render(request, 'listings/listings.html', context)

def listing(request, listing_id: int):

    listing = get_object_or_404(Listing, pk=listing_id)

    context = {
        "listing": listing
    }

    return render(request, 'listings/listing.html', context)

def search(request):
    return render(request, 'listings/search.html')
