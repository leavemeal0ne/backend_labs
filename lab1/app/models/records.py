from sqlalchemy import func

from app.database.database import db


class RecordsModel(db.Model):
    __tablename__ = "records"

    id = db.Column(db.Integer, primary_key=True )
    user_id = db.Column(
        db.Integer,
        db.ForeignKey("users.id"),
        unique=False,
        nullable=False
    )
    category_id = db.Column(
        db.Integer,
        db.ForeignKey("categories.id"),
        unique=False,
        nullable=False
    )
    created_at = db.Column(db.TIMESTAMP, server_default=func.now())
    sum = db.Column(db.Float(precision=2), unique=False, nullable=False)

    user = db.relationship("UsersModel", back_populates="record")
    category = db.relationship("CategoriesModel", back_populates="record")
