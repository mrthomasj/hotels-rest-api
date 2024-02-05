from flask_restful import Resource, reqparse
from models.users import UserModel


class User(Resource):

    def get(self, user_id):
        user = UserModel.find_user(user_id)
        if user:
            return user.json(), 200
        return {'message': f'User_Id {user_id} not found.'}, 404

    def delete(self, user_id):
        user = UserModel.find_user(user_id)

        if hotel:

            try:
                hotel.delete_hotel()
            except Exception as e:
                return {'message': f'An error occurred while performing a database operation. Error: {e}'}, 500

            return {'message': f'Hotel_Id {hotel_id} deleted successfully'}, 200
        return {'message': f'Hotel_Id {hotel_id} does not exist.'}, 400


class Hotels(Resource):
    def get(self):
        return {'hotels': [hotel.json() for hotel in UserModel.query.all()]}, 200
