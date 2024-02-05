from flask_restful import Resource, reqparse
from models import HotelModel


class Hotel(Resource):
    def get(self):
        pass

    def post(self, hotel_id):
        if HotelModel.find_hotel(hotel_id):
            return {'message': f'Hotel_Id {hotel_id} already exists.'}, 400

        arguments = reqparse.RequestParser()
        arguments.add_argument('name')
        arguments.add_argument('stars')
        arguments.add_argument('daily_price')
        arguments.add_argument('city')

        data = arguments.parse_args()

        new_hotel = {
            'hotel_id' : hotel_id,
            'name' : data['name'],
            'stars' : data['stars'],
            'daily_price' : data['daily_price']
            'city' : data['city']
        }

        
