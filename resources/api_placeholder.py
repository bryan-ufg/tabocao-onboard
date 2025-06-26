from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import IntegrityError

from db import db

from models import APIPlaceholderModel
from schemas import APIPlaceholderSchema

blp = Blueprint("APIPlaceholder", "api_placeholder", description="Operations on API Placeholder")

@blp.route("/api_placeholder")
class APIPlaceholderList(MethodView):
    @blp.response(200, APIPlaceholderSchema(many=True))
    def get(self):
        return APIPlaceholderModel.query.order_by(APIPlaceholderModel.updated_at.desc()).limit(15).all()


    @blp.arguments(APIPlaceholderSchema)
    @blp.response(201)
    def post(self, api_placeholder_data):
        api_placeholder = APIPlaceholderModel(**api_placeholder_data)

        try:
            db.session.add(api_placeholder)
            db.session.commit()
        except IntegrityError as e:
            db.session.rollback()
            abort(400, message=str(e))
        
        return {"message": "External Data created successfully."}, 201


@blp.route("/api_placeholder/<int:api_placeholder_id>")
class APIPlaceholder(MethodView):
    @blp.response(200, APIPlaceholderSchema)
    def get(self, api_placeholder_id):
        api_placeholder = APIPlaceholderModel.query.get_or_404(api_placeholder_id)
        return api_placeholder

    @blp.response(204)
    def delete(self, api_placeholder_id):
        api_placeholder = APIPlaceholderModel.query.get_or_404(api_placeholder_id)

        try:
            db.session.delete(api_placeholder)
            db.session.commit()
        except IntegrityError as e:
            db.session.rollback()
            abort(400, message=str(e))
