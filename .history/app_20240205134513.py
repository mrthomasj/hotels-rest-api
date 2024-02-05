from flask import Flask
from flask_restful import Api
from resources.hotel import Hoteis

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///hotels.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
api = Api(app)


api.add_resource(Hoteis, '/hoteis')

if !app.got_first_request:


if __name__ == '__main__':
    from database.database_services import db
    db.init_app(app)
    db.create_all()
    app.run(debug=True)
