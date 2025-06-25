from flask import jsonify
from flask.views import MethodView
from flask_smorest import Blueprint

from models.mock_data import indicators

blp = Blueprint("Indicators", "indicators", description="Mock Indicators")

@blp.route("/api/indicators")
class IndicatorResource(MethodView):
    @blp.response(200)
    def get(self):
        return jsonify(indicators)