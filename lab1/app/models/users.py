from app.database.database import db

class UsersModel(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True, nullable=False)

    record = db.relationship("RecordsModel",back_populates="user", lazy="dynamic")