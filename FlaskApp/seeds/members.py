from models import Member, db
"""

    member_type = Enum('banned', 'regular', 'admin', name='member_type')

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    username = db.Column(db.String(50), nullable=False, unique=True)
    email = db.Column(db.String(50), nullable=False, unique=True)
    club_id = db.Column(db.Integer)
    member_info = db.Column( member_type)
    last_login = db.Column(db.DateTime)
    password_digest = db.Column(db.String(50), nullable=False)
"""
def seed_members():
    demo = Member(
        name='Demo Member', username='demomember', email='demo@lunchclub.com',
        password='password', club_id=1, member_info='regular'
        )
    another_member = Member(
        name='Another Member', username='another_member', email='another_member@lunchclub.com',
        password='password', club_id=1, member_info='admin'
    )
    yet_another_member = Member(
        name='Miembro', username='miembro', email='bestmember@lunchclub.com',
        password='password', club_id=2, member_info='regular'
    )

    db.session.add(demo)
    db.session.add(another_member)
    db.session.add(yet_another_member)

    db.session.commit()


if __name__ == '__main__':
    with app.app_context():
        seed_members()
