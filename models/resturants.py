from db import db


class Restaurant(db.Model):
    __tablename__ = 'restaurant'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(50), nullable=True)
    phone = db.Column(db.Integer, nullable=False)
    location = db.Column(db.String(20), nullable=False)
    restaurant_name = db.Column(db.String(200), nullable=False)
    no_of_seats = db.Column(db.Integer, nullable=False)
    bookings = db.relationship('Bookings', backref='restaurant_booking', lazy=True)

    def to_json(self):
        return dict(restaurant_id=self.id, email=self.email, phone=self.phone, location=self.location,
                    name=self.restaurant_name, no_of_seats=self.no_of_seats)

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
