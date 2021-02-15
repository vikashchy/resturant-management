from flask_restful import Api

from resources.booking_resource import BookingList, BookingResource
from resources.customer_resource import CustomerResource
from resources.resturant_resource import RestaurantList, RestaurantResource

api = Api()
api.add_resource(BookingResource, '/booking', '/booking/<string:booking_id>')
api.add_resource(BookingList, '/bookings')
api.add_resource(RestaurantResource, '/restaurant', '/restaurant/<string:restaurant_id>')
api.add_resource(RestaurantList, '/restaurants')
api.add_resource(CustomerResource, '/customer', '/customer/<string:customer_id>')
