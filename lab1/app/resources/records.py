from datetime import datetime
from flask_smorest import Blueprint, abort
from flask import request,jsonify
from flask.views import MethodView
from app.database.database import *
from app.schemas import *

blp = Blueprint("records", __name__,description="Operations on records")


@blp.route('/records/<int:user_id>')
class Records_By_User(MethodView):
    @blp.response(200, RecordSchema)
    def get(self,user_id):
        record_by_user = list(filter(lambda t: t['user_id'] == user_id, RECORDS))
        if len(record_by_user) == 0:
            abort(404,message="The user has no records")
        else:
            return jsonify({'records_by_user': record_by_user})


@blp.route('/records/<int:user_id>/<int:category_id>')
class Records_By_User_And_Category(MethodView):
    @blp.response(200, RecordSchema)
    def get(self,user_id,category_id):
        record_by_user = list(filter(lambda t: t['user_id'] == user_id, RECORDS))
        if len(record_by_user) == 0:
            abort(404,message="The user has no records")
        record_by_category_and_user = list(filter(lambda t: t['category_id'] == category_id, record_by_user))
        if len(record_by_category_and_user) == 0:
            abort(404,message="The user has no records in this category")
        else:
            return jsonify({'records_by_user_and_category': record_by_category_and_user})

@blp.route('/records')
class Records(MethodView):
    @blp.arguments(RecordSchema)
    @blp.response(200, RecordSchema)
    def post(self,user_data):
        if not request.json:
            abort(404)
        category = list(filter(lambda t: t['id'] == request.json.get('category_id'), CATEGORIES))
        if len(category) == 0:
            abort(404,message="No such category")
        users = list(filter(lambda t: t['id'] == request.json.get('user_id'), USERS))
        if len(users) == 0:
            abort(404,message="The user is not exist")
        record = {
            'id': RECORDS[-1]['id'] + 1,
            'user_id': request.json.get('user_id'),
            'category_id': request.json.get('category_id'),
            'date_time': datetime.now(),
            'total': request.json.get('total')
        }
        RECORDS.append(record)
        return jsonify({'record': record})


