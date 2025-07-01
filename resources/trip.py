from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import IntegrityError

from extensions import db

from models import TripModel
from schemas import TripSchema

blp = Blueprint("Trips", "trips", description="Operations on trips")

@blp.route("/trip")
class TripList(MethodView):
    @blp.response(200, TripSchema(many=True))
    def get(self):
        return TripModel.query.all()

    @blp.arguments(TripSchema)
    @blp.response(201)
    def post(self, trip_data):
        trip = TripModel(**trip_data)

        try:
            db.session.add(trip)
            db.session.commit()
        except IntegrityError:
            db.session.rollback()
            abort(400, message="Invalid Driver or Truck ID.")
        
        return {"message": "Trip created successfully."}, 201


@blp.route("/trip/<int:trip_id>")
class Trip(MethodView):
    @blp.response(200, TripSchema)
    def get(self, trip_id):
        trip = TripModel.query.get_or_404(trip_id)
        return trip

    @blp.response(204)
    def delete(self, trip_id):
        trip = TripModel.query.get_or_404(trip_id)

        try:
            db.session.delete(trip)
            db.session.commit()
        except IntegrityError as e:
            db.session.rollback()
            abort(400, message=str(e))
