from models import db, User

def seed_users():
    demo = User(
        name='Demo User', username='demouser', email='demo@lunchclub.com', password='password', club_id=1,
        )
    another_user = User(
        name='Another User', username='another_user', email='another_user@lunchclub.com', password='password', club_id=2
    )

    db.session.add(demo)

    db.session.commit()
