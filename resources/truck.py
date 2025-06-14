from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import IntegrityError

from db import db

from models import TruckModel
from schemas import TruckSchema

blp = Blueprint("Trucks", "trucks", description="Operations on trucks")

@blp.route("/truck")
class TruckList(MethodView):
    @blp.response(200, TruckSchema(many=True))
    def get(self):
        return TruckModel.query.all()

    @blp.arguments(TruckSchema)
    @blp.response(201)
    def post(self, truck_data):
        truck = TruckModel(**truck_data)

        try:
            db.session.add(truck)
            db.session.commit()
        except IntegrityError as e:
            db.session.rollback()
            abort(400, message=str(e))
        
        return {"message": "Truck created successfully."}, 201


@blp.route("/truck/<int:truck_id>")
class Truck(MethodView):
    @blp.response(200, TruckSchema)
    def get(self, truck_id):
        truck = TruckModel.query.get_or_404(truck_id)
        return truck

    @blp.response(204)
    def delete(self, truck_id):
        truck = TruckModel.query.get_or_404(truck_id)

        try:
            db.session.delete(truck)
            db.session.commit()
        except IntegrityError as e:
            db.session.rollback()
            abort(400, message=str(e))
