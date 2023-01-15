from flask_jwt_extended import jwt_required
from flask_smorest import Blueprint, abort
from flask.views import MethodView
from sqlalchemy.exc import IntegrityError
from app.models import *
from app.database.database import *
from app.schemas import *


blp = Blueprint("categories", __name__,description="Operations on categories")

@blp.route('/categories/<int:categories_id>')
class Categories_id(MethodView):
    @blp.response(200, CategorySchema)
    def get(self,categories_id):
        category = CategoriesModel.query.get_or_404(categories_id)
        return category

@blp.route('/categories')
class Categories(MethodView):
    @blp.response(200, CategorySchema(many=True))
    def get(self):
        return CategoriesModel.query.all()

    @jwt_required()
    @blp.arguments(CategorySchema)
    @blp.response(200, CategorySchema)
    def post(self,category_data):
        category = CategoriesModel(**category_data)
        try:
            db.session.add(category)
            db.session.commit()
        except IntegrityError:
            abort(
                400,
                message="This category already exist"
            )

        return category




