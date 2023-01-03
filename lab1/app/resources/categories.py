from flask_smorest import Blueprint, abort
from flask import request,jsonify
from flask.views import MethodView
from app.database.database import *
from app.schemas import *

blp = Blueprint("categories", __name__,description="Operations on categories")

@blp.route('/categories/<int:categories_id>')
class Categories_id(MethodView):
    @blp.response(200, CategorySchema)
    def get(self,categories_id):
        category = list(filter(lambda t: t['id'] == categories_id, CATEGORIES))
        if len(category) == 0:
            abort(404, message="No such category")
        else:
            return jsonify({'categories': category[0]})

@blp.route('/categories')
class Categories(MethodView):
    @blp.response(200, CategorySchema(many=True))
    def get(self):
        return jsonify({'categories': CATEGORIES})
    @blp.arguments(CategorySchema)
    @blp.response(200, CategorySchema)
    def post(self,user_data):
        if request.json["category_name"] in [u["category_name"] for u in CATEGORIES]:
            abort(400, message="This category is already exist")
        category = {
            'id': CATEGORIES[-1]['id'] + 1,
            'category_name': request.json.get('category_name')
        }
        CATEGORIES.append(category)
        return jsonify({'category': category}), 201




