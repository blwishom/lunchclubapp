from models import Restaurant, db

def seed_restaurants():
    demo = Restaurant(
        name='Vinny\'s Pizzeria', address='123 Piatza Way, Sonoma, CA 54321'
    )
    second_demo = Restaurant(
        name='Anatolia Cafe and Hookah Lounge', address='52 Peachtree St. NW, Atlanta, GA, 30303'
    )

    db.session.add(demo)
    db.session.add(second_demo)
    db.session.commit()
