from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import IntegrityError

from extensions import db

from models import TruckMaintenanceModel
from schemas import TruckMaintenanceSchema

blp = Blueprint("TruckMaintenance", "truck_maintenance", description="Operations on Truck Maintenances")

@blp.route("/truck_maintenance")
class TruckMaintenanceList(MethodView):
    @blp.response(200, TruckMaintenanceSchema(many=True))
    def get(self):
        return TruckMaintenanceModel.query.all()

    @blp.arguments(TruckMaintenanceSchema)
    @blp.response(201)
    def post(self, truck_maintenance_data):
        truck_maintenance = TruckMaintenanceModel(**truck_maintenance_data)

        try:
            db.session.add(truck_maintenance)
            db.session.commit()
        except IntegrityError:
            db.session.rollback()
            abort(400, message="Invalid Truck ID.")
        
        return {"message": "Truck Maintenance created successfully."}, 201


@blp.route("/truck_maintenance/<int:truck_maintenance_id>")
class TruckMaintenance(MethodView):
    @blp.response(200, TruckMaintenanceSchema)
    def get(self, truck_maintenance_id):
        truck_maintenance = TruckMaintenanceModel.query.get_or_404(truck_maintenance_id)
        return truck_maintenance

    @blp.response(204)
    def delete(self, truck_maintenance_id):
        truck_maintenance = TruckMaintenanceModel.query.get_or_404(truck_maintenance_id)

        try:
            db.session.delete(truck_maintenance)
            db.session.commit()
        except IntegrityError as e:
            db.session.rollback()
            abort(400, message=str(e))
