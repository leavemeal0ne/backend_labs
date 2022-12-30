from app import app
from flask_smorest import Api
from app.resources.users import blp as UserBluePrint
from app.resources.categories import blp as CategoriesBluePrint
from app.resources.records import blp as RecordsBluePrint


api = Api(app)
api.register_blueprint(UserBluePrint)
api.register_blueprint(CategoriesBluePrint)
api.register_blueprint(RecordsBluePrint)










