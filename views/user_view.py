from flask import Blueprint, jsonify, request
from models.user_model import User
from database.__init__ import database
import json


user = Blueprint("user", __name__)


@user.route("/users/", methods=["POST"])
def create():

    data = json.loads(request.data)

    print(data)
    my_user = User()
    my_user.name = "Renan"
    my_user.email = "renan@gmail.com"
    my_user.password = "123456"

    # my_user = User()
    # my_user.name = data["username"]
    # my_user.email = data["email"]
    # my_user.password = data["password"]

    created_user = database["PROJECT0"]["users"].insert_one(my_user.__dict__)

    return jsonify({'id': str(created_user.inserted_id)})
