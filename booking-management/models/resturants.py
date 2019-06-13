class ResturantModel:
    def __init__(self, name, location, email, phone, no_of_seats):
        self.name = name
        self.location = location
        self.email = email
        self.phone = phone
        self.no_of_seats = no_of_seats

    def booking(self):
        pass

    def seatquery(self):
        pass

    def cancellation(self):
        pass

    def json(self):
        return {'name': self.name, 'location': self.location, 'email': self.email, 'phone': self.phone,
                'max_seats': self.no_of_seats}
