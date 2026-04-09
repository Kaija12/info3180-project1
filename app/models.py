from . import db

class Property(db.Model):
    __tablename__ = 'properties'

    id          = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title       = db.Column(db.Text, nullable=False)
    description = db.Column(db.Text, nullable=False)
    no_of_rooms = db.Column(db.Text, nullable=False)
    no_of_bathrooms = db.Column(db.Text, nullable=False)
    price       = db.Column(db.Text, nullable=False)
    prop_type   = db.Column(db.String(50), nullable=False)   # 'House' or 'Apartment'
    location    = db.Column(db.Text, nullable=False)
    photo       = db.Column(db.String(255), nullable=False)  # filename only

    def __repr__(self):
        return f'<Property {self.title}>'