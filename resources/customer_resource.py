from flask import request
from flask_restful import Resource

from models.customer import Customer


class CustomerResource(Resource):
    def get(self, customer_id):
        customer = Customer.query.filter_by(id=customer_id).first()
        if customer:
            return customer.to_json(), 200
        else:
            return "Customer not found", 404

    def post(self):
        cust_email = request.json['email']
        cust_name = request.json['name']
        cust_address = request.json['address']
        cust_phone = request.json['phone']
        customer = Customer(email=cust_email, name=cust_name, address=cust_address, phone=cust_phone)
        customer.save_to_db()
        return customer.to_json(), 201

    def patch(self, customer_id):
        customer = Customer.query.filter_by(id=customer_id).first()
        customer.email = request.json.get('email') or customer.email
        customer.name = request.json.get('name') or customer.name
        customer.address = request.json.get('address') or customer.address
        customer.phone = request.json.get('phone') or customer.phone
        customer.save_to_db()
        return customer.to_json(), 200

    def delete(self, customer_id):
        customer = Customer.query.filter_by(id=customer_id).first()
        if customer:
            customer.delete_customer()
            return {'Message': f'Customer deleted successfully with customer id: {customer_id}'}, 200
        else:
            return {'Message': f'Customer not found with customer id: {customer_id} '}, 200
