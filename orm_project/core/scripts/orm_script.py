from core.models import Restaurant, Rating, Sale
from django.utils import timezone
from django.db import connection
from django.contrib.auth.models import User
from pprint import pprint

def run():
    user = User.objects.first()
    restaurant = Restaurant.objects.first()

    rating = Rating(
        user=user,
        restaurant=restaurant,
        rating=0
    )
    rating.full_clean()
    rating.save()