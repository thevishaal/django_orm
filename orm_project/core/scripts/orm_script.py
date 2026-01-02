from core.models import Restaurant, Rating, Sale
from django.utils import timezone
from django.db import connection
from django.contrib.auth.models import User
from pprint import pprint

def run():
    
    restaurant = Restaurant.objects.first()

    print(restaurant.name)

    restaurant.name = 'New Restaurant Name'
    restaurant.save(update_fields=['name'])
    print(connection.queries)