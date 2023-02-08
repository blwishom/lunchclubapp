from models import db, Member

def seed_members():
    demo = Member(
        name='Demo Member', username='demomember', email='demo@lunchclub.com', password='password', club_id=1,
        )
    another_member = Member(
        name='Another Member', username='another_member', email='another_member@lunchclub.com', password='password', club_id=2
    )

    db.session.add(demo)

    db.session.commit()
