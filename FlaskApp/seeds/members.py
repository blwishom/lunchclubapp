from models import Member, db
"""

    member_type = Enum('banned', 'regular', 'admin', name='member_type')

    __tablename__ = 'members'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False, unique=True)
    club_id = db.Column(db.Integer, db.ForeignKey('clubs.id'))
    member_info = db.Column( member_type)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), unique=True, nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(
        db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    user = relationship("User", back_populates="members")
"""
def seed_members():
    demo = Member(
        name='Demo Member', user_id=1, email='demo@lunchclub.com', club_id=1, member_info='regular'
        )
    another_member = Member(
        name='Another Member', user_id=2, email='another_member@lunchclub.com',
        club_id=1, member_info='admin'
    )
    yet_another_member = Member(
        name='Miembro', user_id=3, email='bestmember@lunchclub.com',
        club_id=2, member_info='regular'
    )
    yet_a_fourth_member = Member(
        name='Member 4', email='fourth@lunchclub.com',
        club_id=2, member_info='banned'
    )

    db.session.add(demo)
    db.session.add(another_member)
    db.session.add(yet_another_member)
    db.session.add(yet_a_fourth_member)

    db.session.commit()


if __name__ == '__main__':
    with app.app_context():
        seed_members()
