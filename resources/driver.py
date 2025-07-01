from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import IntegrityError

from extensions import db

from models import DriverModel
from schemas import DriverSchema

blp = Blueprint("Drivers", "drivers", description="Operations on drivers")

@blp.route("/driver")
class DriverList(MethodView):
    @blp.response(200, DriverSchema(many=True))
    def get(self):
        return DriverModel.query.all()

    @blp.arguments(DriverSchema)
    @blp.response(201)
    def post(self, driver_data):
        driver = DriverModel(**driver_data)

        try:
            db.session.add(driver)
            db.session.commit()
        except IntegrityError as e:
            db.session.rollback()
            abort(400, message=str(e))
        
        return {"message": "Driver created successfully."}, 201


@blp.route("/driver/<int:driver_id>")
class Driver(MethodView):
    @blp.response(200, DriverSchema)
    def get(self, driver_id):
        driver = DriverModel.query.get_or_404(driver_id)
        return driver

    @blp.response(204)
    def delete(self, driver_id):
        driver = DriverModel.query.get_or_404(driver_id)

        try:
            db.session.delete(driver)
            db.session.commit()
        except IntegrityError as e:
            db.session.rollback()
            abort(400, message=str(e))
