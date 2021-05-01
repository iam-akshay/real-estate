from django.shortcuts import render
from django.http import HttpResponse
from listings.models import Listing
from realtors.models import Realtor


def page_home(request):
    listings = Listing.objects.order_by("-list_date").filter(is_published=True)[:3]

    context = {"listings": listings}
    return render(request, "pages/home.html", context)


def page_about(request):
    realtors = Realtor.objects.all()
    realtors_mvp = Realtor.objects.filter(is_mvp=True)
    context = {
        "realtors": realtors,
        "realtors_mvp": realtors_mvp
    }
    return render(request, "pages/about.html", context)
