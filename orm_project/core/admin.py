from django.contrib import admin
from core.models import Restaurant, Sale, Rating


class RatingInline(admin.TabularInline):
    model = Rating
    extra = 1

class SaleInline(admin.TabularInline):
    model = Sale
    extra = 1

class RestaurantAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['name', 'website']}),
        ('Date Information', {'fields': ['date_opened']}),
        ('Restaurant Address', {'fields': ['latitude', 'longitude']}),
        ('Choices', {'fields': ['restaurant_type']})
    ]
    inlines = [RatingInline, SaleInline]

    list_display = ["name", "website", "date_opened", "restaurant_type"]
    list_filter = ["date_opened", "name"]
    search_fields = ["name", "restaurant_type"]
    list_display_links = ["name", "website", "restaurant_type"]

admin.site.register(Restaurant, RestaurantAdmin)
# admin.site.register(Sale)
# admin.site.register(Rating)