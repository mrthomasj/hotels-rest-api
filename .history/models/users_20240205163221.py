from database.database_services import db


class UserModel(db.Model):
    __tablename__ = 'users'

    user_id = db.Column(db.String, primary_key=True)
    username = db.Column(db.String(20))
    password = db.Column(db.String(16))

    def __init__(self, user_id, username, password):
        self.user_id = user_id
        self.username = username
        self.password = password

    def json(self):
        return {
            'user_id': self.user_id,
            'username': self.username,
            'password': self.password
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
