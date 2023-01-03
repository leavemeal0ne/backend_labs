from flask_smorest import Blueprint, abort
from flask.views import MethodView
from app.database.database import *
from app.schemas import *
from app.models import *
from sqlalchemy.exc import IntegrityError

blp = Blueprint("users", __name__, description="Operations on users")


@blp.route("/users/<int:user_id>")
class Users_id(MethodView):
    @blp.response(200, UserSchema)
    def get(self, user_id):
        user = UsersModel.query.get_or_404(user_id)
        return user

    @blp.response(200, UserSchema)
    def delete(self, user_id):
        try:
            del_user = USERS[user_id]
            del USERS[user_id]
            return del_user
        except KeyError:
            abort(404, message="User not found")


@blp.route("/users")
class UserList(MethodView):
    @blp.response(200, UserSchema(many=True))
    def get(self):
        return UsersModel.query.all()

    @blp.arguments(UserSchema)
    @blp.response(200, UserSchema)
    def post(self, user_data):
        user = UsersModel(**user_data)
        try:
            db.session.add(user)
            db.session.commit()
        except IntegrityError:
            abort(
                400,
                message="This user already exist"
            )

        return user
