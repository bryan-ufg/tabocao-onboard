from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import IntegrityError

from db import db

from models import ASOModel
from schemas import ASOSchema

blp = Blueprint("ASO", "aso", description="Operations on ASOs")

@blp.route("/aso")
class ASOList(MethodView):
    @blp.response(200, ASOSchema(many=True))
    def get(self):
        return ASOModel.query.all()

    @blp.arguments(ASOSchema)
    @blp.response(201)
    def post(self, aso_data):
        aso = ASOModel(**aso_data)

        try:
            db.session.add(aso)
            db.session.commit()
        except IntegrityError:
            db.session.rollback()
            abort(400, message="Invalid Driver ID.")
        
        return {"message": "ASO created successfully."}, 201


@blp.route("/aso/<int:aso_id>")
class ASO(MethodView):
    @blp.response(200, ASOSchema)
    def get(self, aso_id):
        aso = ASOModel.query.get_or_404(aso_id)
        return aso

    @blp.response(204)
    def delete(self, aso_id):
        aso = ASOModel.query.get_or_404(aso_id)

        try:
            db.session.delete(aso)
            db.session.commit()
        except IntegrityError as e:
            db.session.rollback()
            abort(400, message=str(e))
