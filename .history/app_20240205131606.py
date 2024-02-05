from flask import Flask
from flask_restful import Api
from resources import Hoteis

app = Flask(__name__)
api = Api(app)

api.add_resource(Hoteis, '/hoteis')


if __name__ == '__main__':
    from database.database_services import db
    db.init_app(app)
    app.run(debug=True)
