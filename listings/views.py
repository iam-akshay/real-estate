from django.shortcuts import render
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
    return render(request, 'listings/listing.html')

def search(request):
    return render(request, 'listings/search.html')
