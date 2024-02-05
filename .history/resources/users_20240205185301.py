from flask_restful import Resource, reqparse
from models.users import UserModel

attributes = reqparse.RequestParser()
attributes.add_argument(
    'username', type=str, required=True, help="The field 'username' must be filled")
attributes.add_argument(
    'password', type=str, required=True, help="The field 'password' must be filled")


class User(Resource):

    def get(self, user_id):
        user = UserModel.find_user(user_id)
        if user:
            return user.json(), 200
        return {'message': f'User_Id {user_id} not found.'}, 404

    def delete(self, user_id):
        user = UserModel.find_user(user_id)

        if user:

            try:
                user.delete_user()
            except Exception as e:
                return {'message': f'An error occurred while performing a database operation. Error: {e}'}, 500

            return {'message': f'User_Id {user_id} deleted successfully'}, 200
        return {'message': f'User_Id {user_id} does not exist.'}, 400


class UserRegister(Resource):
    def post(self):
        user_data = attributes.parse_args()

        if UserModel.find_by_username(user_data['username']):
            return {'message': f"The username '{user_data['username']} already exists."}, 400

        user = UserModel(**user_data)

        try:
            user.save_user()
        except Exception as e:
            return {'message': f'An error occurred while performing a database operation. Error: {e}'}, 500

        return {'message': 'User created successfully'}, 201


class UserLogin(Resource):
    @classmethod
    def post(cls):
        user_data = attributes.parse_args()

        user = UserModel.find_by_username(user_data['username'])

        if user and safe_str_cmp(user.password, user_data['password']):
            access_token = create_token(identity=user.user_id)
