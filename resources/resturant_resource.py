from flask import request
from flask_restful import Resource

from models import Restaurant


class RestaurantResource(Resource):
    @classmethod
    def get(cls, restaurant_id):
        restaurant = Restaurant.query.filter_by(id=restaurant_id).first()
        if restaurant:
            return restaurant.to_json(), 200
        else:
            return f'Restaurant id:{restaurant} not found !!!', 404

    @classmethod
    def post(cls):
        restaurant_name = request.json['name']
        location = request.json['location']
        phone = request.json['phone']
        email = request.json['email']
        no_of_seats = request.json['max_seats']
        restaurant = Restaurant(email=email, phone=phone, location=location, restaurant_name=restaurant_name,
                                no_of_seats=no_of_seats)
        restaurant.save_to_db()
        return restaurant.to_json(), 201


class RestaurantList(Resource):
    @classmethod
    def get(cls):
        return [x.to_json() for x in Restaurant.query.all()]
