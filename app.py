from flask import Flask, jsonify
from flask_restful import Api
from flask_jwt_extended import JWTManager
from resources.hotel import Hotel, Hotels
from resources.users import User, UserRegister, UserLogin, UserLogout
from blocklist import BLOCKLIST


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///hotels.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = 'ThisIsaSecret'
app.config['JWT_BLOCKLIST_ENABLED'] = True
api = Api(app)
jwt = JWTManager(app)


api.add_resource(Hotel, '/hotel', '/hotel/<string:hotel_id>')
api.add_resource(Hotels, '/hotels')
api.add_resource(User, '/users/<int:user_id>')
api.add_resource(UserRegister, '/register')
api.add_resource(UserLogin, '/login')
api.add_resource(UserLogout, '/logout')


@jwt.token_in_blocklist_loader
def check_blocklist(self, token):
    return token['jti'] in BLOCKLIST


@jwt.revoked_token_loader
def access_token_invalidated(jwt_header, jwt_payload):
    return jsonify({'message': 'You have been logged out.'}), 401


if __name__ == '__main__':
    from database.database_services import db
    db.init_app(app)
    with app.app_context():
        db.create_all()
    app.run(debug=True)
