import datetime

import jwt
from flask import request, jsonify
from flask_jwt_extended import create_access_token, jwt_required
from flask_smorest import Blueprint, abort
from flask.views import MethodView
from passlib.handlers.pbkdf2 import pbkdf2_sha256
from werkzeug.security import generate_password_hash, check_password_hash

from app import app
from app.database.database import *
from app.schemas import *
from app.models import *
from sqlalchemy.exc import IntegrityError

blp = Blueprint("users", __name__, description="Operations on users")


@blp.route("/users/<int:user_id>")
class Users_id(MethodView):
    @jwt_required()
    @blp.response(200, UserSchema)
    def get(self, user_id, ):
        user = UsersModel.query.get_or_404(user_id)
        return user

@blp.route("/users")
class UserList(MethodView):
    @blp.response(200, UserSchema(many=True))
    def get(self):
        print("xD")
        return UsersModel.query.all()
@blp.route("/register")
class Register(MethodView):
    @blp.arguments(UserSchema)
    @blp.response(200, UserSchema)
    def post(self, user_data):
        new_user = UsersModel(
            username=user_data["username"],
            password=pbkdf2_sha256.hash(user_data["password"]),
        )
        try:
            db.session.add(new_user)
            db.session.commit()
        except IntegrityError:
            abort(400, message="User with such username already exists")

        return new_user
@blp.route("/login")
class Login(MethodView):
    def post(self):
        auth = request.authorization
        user = UsersModel.query.filter_by(username=auth["username"]).first()
        if user and pbkdf2_sha256.verify(auth["password"], user.password):

           access_token  = create_access_token(identity=user.id)
           return jsonify({'access_token': access_token})
        else:
            abort(400, "Incorrect login or password")