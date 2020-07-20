from app import db


class Skill(db.Model):
    __tablename__ = 'results'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    followers_count = db.Column(db.Integer)

    def __init__(self, name):
        self.name = name
        self.followers_count = 0

    def __repr__(self):
        return f'<id {self.id} - {self.name}>'

