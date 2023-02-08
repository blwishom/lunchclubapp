from models import Club, db
"""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False, unique=True)
    location = db.Column(db.String(50), nullable=False)
    join_code = db.Column(db.String(6), nullable=False, default=000000)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow)

"""


def seed_clubs():
    demo = Club(
        name='The Club Sandwich Club', location='Reston, VA', join_code=123456
    )
    another_club = Club(
        name='H & R Block of Annapolis', location='Annapolis, MD', join_code=123456
    )

    db.session.add(demo)
    db.session.add(another_club)


    db.session.commit()


if __name__ == '__main__':
    with app.app_context():
        seed_clubs()
