from datetime import datetime
from flask import request
from flask_restful import Resource

from models.bookings import Bookings


class BookingResource(Resource):
    @classmethod
    def get(cls, booking_id):
        booking = Bookings.query.filter_by(id=booking_id).first()
        if booking:
            return booking.to_json(), 200
        else:
            return f'Booking id:{booking_id} not found !!!', 404

    @classmethod
    def post(cls):
        username = request.json['user_name']
        restaurant_id = request.json['restaurant_id']
        phone = request.json['phone']
        email = request.json['email']
        no_of_seats = request.json['no_of_seats']
        booking_date = datetime.strptime(request.json['booking_date'], '%d/%m/%Y')
        customer_id = request.json['customer_id']
        message = f'Booking confirmed for today for {username} at {restaurant_id} for {no_of_seats} people \n. We ' \
                  f' will contact you on phone no: {phone} & email :{email} with further details.'
        booking = Bookings(cust_name=username, no_of_seats=no_of_seats, booking_date=booking_date,
                           restaurant_id=restaurant_id, customer_id=customer_id)
        booking.save_to_db()
        return booking.to_json(), 201

    @classmethod
    def patch(cls):
        return 'patch_request'

    @classmethod
    def delete(cls, booking_id):
        booking = Bookings.query.filter_by(id=booking_id).first()
        if booking:
            booking.delete_booking()
            return {'Message': f'Booking deleted successfully with booking id: {booking_id}'}, 200
        else:
            return {'Message': f'Booking id:{booking_id} not found !!!'}, 404


class BookingList(Resource):
    def get(self):
        return [booking.all_list() for booking in Bookings.query.all()]
