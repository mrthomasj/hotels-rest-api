from database.database_services import db


class HotelModel(db.Model):
    __tablename__ = 'hoteis'

    hotel_id = db.Column(db.String, primary_key=True)
    name = db.Column(db.String(80))
    stars = db.Column(db.Float(precision=1))
    daily_price = db.Column(db.Float(precision=2))
    city = db.Column(db.String(40))

    def __init__(self, hotel_id, name, stars, daily_price, city):
        self.hotel_id = hotel_id
        self.name = name
        self.stars = stars
        self.daily_price = daily_price
        self.city = city

    def get_all():
        pass
