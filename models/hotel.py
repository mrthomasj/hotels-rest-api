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

    def json(self):
        return {
            'hotel_id': self.hotel_id,
            'name': self.name,
            'stars': self.stars,
            'daily_price': self.daily_price,
            'city': self.city
        }

    @classmethod
    def find_hotel(cls, hotel_id):
        hotel = cls.query.filter_by(hotel_id=hotel_id).first()
        if hotel:
            return hotel
        return None

    def save_hotel(self):
        db.session.add(self)
        db.session.commit()

    def update_hotel(self, name, stars, daily_price, city):
        self.name = name
        self.stars = stars
        self.daily_price = daily_price
        self.city = city

    def delete_hotel(self):
        db.session.delete(self)
        db.session.commit()
