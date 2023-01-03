
from sqlalchemy.exc import IntegrityError
from flask_smorest import Blueprint, abort
from flask.views import MethodView
from app.database.database import *
from app.schemas import *
from app.models import *

blp = Blueprint("records", __name__,description="Operations on records")


@blp.route('/records/<int:user_id>')
class Records_By_User(MethodView):
    @blp.response(200, RecordSchema(many=True))
    def get(self,user_id):
        return RecordsModel.query.filter_by(user_id=user_id).all()


@blp.route('/records/<int:user_id>/<int:category_id>')
class Records_By_User_And_Category(MethodView):
    @blp.response(200, RecordSchema(many=True))
    def get(self,user_id,category_id):
        return RecordsModel.query.filter_by(user_id=user_id,category_id=category_id).all()

@blp.route('/records')
class Records(MethodView):
    @blp.arguments(RecordSchema)
    @blp.response(200, RecordSchema)
    def post(self,record_data):
        record = RecordsModel(**record_data)
        try:
            db.session.add(record)
            db.session.commit()
        except IntegrityError:
            abort(
                400,
                message="Incorrect fields "
            )
        return record

