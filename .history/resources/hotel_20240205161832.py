from flask_restful import Resource, reqparse
from models.hotel import HotelModel


class Hotel(Resource):
    arguments = reqparse.RequestParser()
    arguments.add_argument('name', type=str, required=True,
                           help="Field 'Name' must be filled")
    arguments.add_argument('stars', type=float, required=True,
                           help="Field 'Stars' must be filled")
    arguments.add_argument('daily_price', type=float, required=True,
                           help="Field 'Daily_price' must be filled")
    arguments.add_argument('city', type=str, required=True,
                           help="Field 'City' must be filled")

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
        try:
            new_hotel.save_hotel()
        except Exception as e:
            return {'message': f'An error occurred while performing a database operation. Error: {e}'}

        return new_hotel.json(), 201

    def put(self, hotel_id):
        data = Hotel.arguments.parse_args()
        hotel = HotelModel.find_hotel(hotel_id)
        if hotel:
            hotel.update_hotel(**data)

            try:
                hotel.save_hotel()
            except Exception as e:
                return {'message': f'An error occurred while performing a database operation. Error: {e}'}

            return hotel.json(), 200
        return {'message': f'Hotel_Id {hotel_id} does not exist.'}, 400

    def delete(self, hotel_id):
        hotel = HotelModel.find_hotel(hotel_id)

        if hotel:
            hotel.delete_hotel()
            return {'message': f'Hotel_Id {hotel_id} deleted successfully'}, 200
        return {'message': f'Hotel_Id {hotel_id} does not exist.'}, 400


class Hotels(Resource):
    def get(self):
        return {'hotels': [hotel.json() for hotel in HotelModel.query.all()]}, 200
