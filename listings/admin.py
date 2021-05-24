from django.contrib import admin

from .models import Listing

# Register your models here.

class ListingAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_published', 'price', 'list_date', 'realtors',)
    # makes them clickable
    list_display_links = ('id', 'title')
    # adds filter
    list_filter = ('realtors',)
    # make boolean values clickable and from here we can publish and publish
    list_editable = ('is_published',)
    # add searching option
    search_fields = ('title', 'description', 'address', 'city', 'state', 'city', 'zipcode', 'price')
    # add pagination
    list_per_page = 25

admin.site.register(Listing, ListingAdmin)