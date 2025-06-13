from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import IntegrityError

from db import db
from crypt import bcrypt

from models import UserModel
from schemas import UserSchema

blp = Blueprint("Users", "users", description="Operations on users")

@blp.route("/user/<int:user_id>")
class User(MethodView):
    @blp.response(200, UserSchema)
    def get(self, user_id):
        user = UserModel.query.get_or_404(user_id)
        return user

    @blp.response(204)
    def delete(self, user_id):
        user = UserModel.query.get_or_404(user_id)

        try:
            db.session.delete(user)
            db.session.commit()
        except IntegrityError as e:
            db.session.rollback()
            abort(400, message=str(e))

@blp.route("/user")
class UserList(MethodView):
    @blp.response(200, UserSchema(many=True))
    def get(self):
        return UserModel.query.all()

    @blp.arguments(UserSchema)
    @blp.response(201)
    def post(self, data):
        hash_pw = bcrypt.generate_password_hash(data["password"]).decode("utf-8")

        user = UserModel(
            name = data["name"],
            username = data["username"],
            password = hash_pw
        )

        try:
            db.session.add(user)
            db.session.commit()
        except IntegrityError as e:
            db.session.rollback()
            abort(400, message=str(e))
        
        return {"message": "User created successfully."}, 201
