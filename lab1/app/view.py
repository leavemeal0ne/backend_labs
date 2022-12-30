from app import app, jsonify, abort, make_response, request
from app.database.database import *
from flask_smorest import Api
from app.resources.users import blp as UserBluePrint
from app.resources.categories import blp as CategoriesBluePrint
from app.resources.records import blp as RecordsBluePrint

app.config["PROPAGATE_EXCEPTIONS"] = True
app.config['API_TITLE'] = "Finance REST API"
app.config["API_VERSION"] = "v1"
app.config["OPENAPI_VERSION"] = "3.0.3"
app.config["OPENAPI_URL_PREFIX"] = "/"

api = Api(app)
api.register_blueprint(UserBluePrint)
api.register_blueprint(CategoriesBluePrint)
api.register_blueprint(RecordsBluePrint)










