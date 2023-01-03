from app.database.database import db


class CurrenciesModel(db.Model):
    __tablename__ = "currencies"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)

    user = db.relationship("UsersModel", back_populates="currency", lazy=True)
    record = db.relationship("RecordsModel",back_populates="currency", lazy=True)