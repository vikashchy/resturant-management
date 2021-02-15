from db import db


class Customer(db.Model):
    __tablename__ = 'customer'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=True)
    email = db.Column(db.String(50), nullable=True)
    address = db.Column(db.String(100), nullable=True)
    phone = db.Column(db.Integer, nullable=False)
    bookings = db.relationship('Bookings', backref='customer_booking', lazy=True)

    def to_json(self):
        return dict(customer_id=self.id, email=self.email, phone=self.phone, location=self.address, name=self.name,
                    bookings=self.bookings_json())

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_customer(self):
        db.session.delete(self)
        db.session.commit()

    def bookings_json(self):
        return [dict(id=booking.id,
                     no_of_seats=booking.no_of_seats,
                     booking_date=str(booking.booking_date),
                     restaurant_details=booking.restaurant.to_json()) for booking in self.bookings]
