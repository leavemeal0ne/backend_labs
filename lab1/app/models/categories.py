from app.database.database import db

class CategoriesModel(db.Model):
    __tablename__ = "categories"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True, nullable=False)

    record = db.relationship("RecordsModel", back_populates="category", lazy="dynamic")