from database.database_services import db


class HotelModel(db.Model):
    __tablename__ = 'hoteis'

    hotel_id = db.Column(db.String, primary_key=True)
    name = db.Column(db.String(80))
    stars = db.Column(db.Float(precision=1))
    daily_price = db.Column(db.Float(precision=2))
    city = db.Column(db.String(40))
