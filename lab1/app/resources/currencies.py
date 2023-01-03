from flask_smorest import Blueprint, abort
from flask.views import MethodView
from sqlalchemy.exc import IntegrityError
from app.models import *
from app.database.database import *
from app.schemas import *

blp = Blueprint("currencies", __name__, description="Operations on currenceis")


@blp.route("/currencies/<int:id>")
class Currency(MethodView):
    @blp.response(200, CurrencySchema)
    def get(self, id):
        currency = CurrenciesModel.query.get_or_404(id)
        return currency


@blp.route("/currencies")
class CurrencyList(MethodView):

    @blp.response(200, CurrencySchema(many=True))
    def get(self):
        return CurrenciesModel.query.all()

    @blp.arguments(CurrencySchema)
    @blp.response(200, CurrencySchema)
    def post(self, currency_data):
        currency = CurrenciesModel(**currency_data)
        try:
            db.session.add(currency)
            db.session.commit()
        except IntegrityError:
            return abort(
                404,
                message="This currency already exists")

        return currency