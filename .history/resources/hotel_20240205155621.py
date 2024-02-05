from flask_restful import Resource, reqparse
from models.hotel import HotelModel


class Hotel(Resource):
    arguments = reqparse.RequestParser()
    arguments.add_argument('name')
    arguments.add_argument('stars')
    arguments.add_argument('daily_price')
    arguments.add_argument('city')

    def get(self, hotel_id):
        hotel = HotelModel.find_hotel(hotel_id)
        if hotel:
            return hotel.json(), 200
        return {'message': f'Hotel_Id {hotel_id} not found.'}, 404

    def post(self, hotel_id):
        if HotelModel.find_hotel(hotel_id):
            return {'message': f'Hotel_Id {hotel_id} already exists.'}, 400

        data = Hotel.arguments.parse_args()

        new_hotel = HotelModel(hotel_id, **data)
        new_hotel.save_hotel()
        return new_hotel.json(), 201

    def put(self, hotel_id):
        data = Hotel.arguments.parse_args()
        hotel = HotelModel.find_hotel(hotel_id)
        if hotel:
            hotel.update_hotel(**data)
            hotel.save_hotel()
            return hotel.json(), 200
        return {'message': f'Hotel_Id {hotel_id} does not exists.'}, 400
