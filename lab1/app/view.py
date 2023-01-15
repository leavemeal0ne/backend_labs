

from flask import jsonify
from flask_jwt_extended import JWTManager

from app import app, db
from flask_smorest import Api

from app.models.currencies import CurrenciesModel
from app.resources.users import blp as UserBluePrint
from app.resources.categories import blp as CategoriesBluePrint
from app.resources.records import blp as RecordsBluePrint
from app.resources.currencies import blp as CurrenciesBluePrint
db.init_app(app)

jwt = JWTManager(app)

@jwt.expired_token_loader
def expired_token_callback(jwt_header, jwt_payload):
   return (
       jsonify({"message": "The token has expired.", "error": "token_expired"}),
       401,
   )

@jwt.invalid_token_loader
def invalid_token_callback(error):
   return (
       jsonify(
           {"message": "Signature verification failed.", "error": "invalid_token"}
       ),
       401,
   )

@jwt.unauthorized_loader
def missing_token_callback(error):
   return (
       jsonify(
           {
               "description": "Request does not contain an access token.",
               "error": "authorization_required",
           }
       ),
       401,
   )

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









