from flask_smorest import Blueprint, abort
from flask import request,jsonify
from flask.views import MethodView
from app.database.database import *
from app.schemas import *
blp = Blueprint("users", __name__,description="Operations on user")

@blp.route("/users/<int:user_id>")
class Users_id(MethodView):
    def get(self,user_id):
        try:
            return USERS[user_id]
        except KeyError:
            abort(404,message="User not found")
    def delete(self,user_id):
        try:
            del_user = USERS[user_id]
            del USERS[user_id]
            return del_user
        except KeyError:
            abort(404,message="User not found")

@blp.route("/users")
class UserList(MethodView):
    def get(self):
        return list(USERS.values)
    @blp.arguments(UserSchema)
    def post(self,user_data):
        if request.json["name"] in [u["name"] for u in USERS]:
            abort(400, message="This name is already exist")
        user = {
            'id': USERS[-1]['id'] + 1,
            'name': request.json.get('name')
        }
        USERS.append(user)
        return jsonify({'user': user}), 201