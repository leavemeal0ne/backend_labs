from app.database.database import db

class UsersModel(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=False)
    password = db.Column(db.String(64),nullable=False)
    currency_id = db.Column(
        db.Integer,
        db.ForeignKey("currencies.id"),
        nullable=False,
        default=1)

    record = db.relationship("RecordsModel",back_populates="user", lazy="dynamic")
    currency = db.relationship("CurrenciesModel", back_populates="user")
