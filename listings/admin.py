from django.contrib import admin
from .models import Listing

@admin.register(Listing)
class ListingAdmin(admin.ModelAdmin):
    list_display = ('title', 'address', 'zipcode', 'city', 'state', 'price', "bedrooms", 'garage', 'is_published', 'list_date')
    list_per_page = 25
    list_editable = ('is_published',)
    list_filter = ('city', 'state')
    search_fields = ('title', 'city', 'state', 'zipcode')
