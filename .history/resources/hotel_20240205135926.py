from flask_restful import Resource
from models import HotelModel


class Hoteis(Resource):
    def get(self):
        pass

    def post(self, hotel_id):
        if HotelModel.find_hotel(hotel_id):
            return {'message': f'Hotel_Id {hotel_id} already exists.'}, 400

        pass
