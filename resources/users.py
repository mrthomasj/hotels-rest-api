import hmac
from flask_restful import Resource, reqparse
from flask_jwt_extended import create_access_token, jwt_required, get_jwt
from models.users import UserModel
from blocklist import BLOCKLIST

attributes = reqparse.RequestParser()
attributes.add_argument(
    'username', type=str, required=True, help="The field 'username' must be filled")
attributes.add_argument(
    'password', type=str, required=True, help="The field 'password' must be filled")


def safe_str_cmp(a: str, b: str) -> bool:
    if isinstance(a, str):
        a = a.encode("utf-8")  # type: ignore

    if isinstance(b, str):
        b = b.encode("utf-8")  # type: ignore
    return hmac.compare_digest(a, b)


class User(Resource):

    def get(self, user_id):
        user = UserModel.find_user(user_id)
        if user:
            return user.json(), 200
        return {'message': f'User_Id {user_id} not found.'}, 404

    @jwt_required()
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
            access_token = create_access_token(identity=user.user_id)
            return {'access_token': access_token}, 200
        return {'message': 'User or Password is incorrect'}, 401


class UserLogout(Resource):

    @jwt_required()
    def post(self):
        jwt_id = get_jwt()['jti']
        BLOCKLIST.add(jwt_id)
        return {'message': 'User logged out.'}, 200
