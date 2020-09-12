from django.contrib import admin
from .models import Category, Listing

class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "category")

class ListingAdmin(admin.ModelAdmin ):
    list_display = ("id", "category", "title", "price", "owner")

# Register your models here.
admin.site.register(Category, CategoryAdmin)
admin.site.register(Listing, ListingAdmin)