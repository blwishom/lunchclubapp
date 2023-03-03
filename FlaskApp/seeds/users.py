from models import User, db

"""
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), nullable=False, unique=True)
    last_login = db.Column(
        db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    password_digest = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(
        db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    members = relationship("Member", uselist=False, back_populates="user")

"""

def seed_users():
    demo = User(
        username='demomember',
        password='password'
        )
    another_user = User(
        username='another_member',
        password='password'
    )
    yet_another_user = User(
        username='miembro',
        password='password'
    )
    yet_a_fourth_user = User(
        username='miembro_miembro',
        password='password'
    )
    yet_a_fifth_user = User(
        username='membre',
        password='password'
    )

    db.session.add(demo)
    db.session.add(another_user)
    db.session.add(yet_another_user)
    db.session.add(yet_a_fourth_user)
    db.session.add(yet_a_fifth_user)


    db.session.commit()


if __name__ == '__main__':
    with app.app_context():
        seed_users()