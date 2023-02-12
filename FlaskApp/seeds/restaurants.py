from models import Restaurant, db

def seed_restaurants():
    demo = Restaurant(
        name='Vinny\'s Pizzeria', address='123 Piatza Way Sonoma, Ca 54321'
    )
