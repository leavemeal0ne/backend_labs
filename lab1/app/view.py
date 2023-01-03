from app import app, db
from flask_smorest import Api

from app.models.currencies import CurrenciesModel
from app.resources.users import blp as UserBluePrint
from app.resources.categories import blp as CategoriesBluePrint
from app.resources.records import blp as RecordsBluePrint
from app.resources.currencies import blp as CurrenciesBluePrint

db.init_app(app)

with app.app_context():
    db.create_all()

    if len(CurrenciesModel.query.all()) == 0:
        currency = CurrenciesModel(name="UAH")
        db.session.add(currency)
        db.session.commit()


api = Api(app)
api.register_blueprint(UserBluePrint)
api.register_blueprint(CategoriesBluePrint)
api.register_blueprint(RecordsBluePrint)
api.register_blueprint(CurrenciesBluePrint)









