from json import dumps

from flask import Blueprint,request,redirect,render_template,jsonify

from data.users import users
from models.user import User

user_controller = Blueprint("user", __name__)
@user_controller.route("/get",methods=["GET"])
def get_users():
    return jsonify([user.__dict__ for user in users])
@user_controller.route("/get/<id>",methods=["GET"])
def get_user(id):
    user = None
    for u in users:
        if u.id == id and isinstance(user,User):
            user = u
    if user:
        return jsonify(user.__dict__)
    return jsonify({"error": f"User with id {id} not found"}), 404

@user_controller.route("/add",methods=["POST"])
def add_user():
    data = request.get_json()
    if isinstance(data,User):
        users.append(data)
        return jsonify(users.__dict__)
    else:
        return jsonify({"error": "Invalid data"}), 400
@user_controller.route("/edit/<id>",methods=["PUT"])
def edit_user(id):
    user = None
    request_body = request.get_json()
    for u in users:
        if u.id == id:
            user = u
    if user and isinstance(user,User):
        user.first_name = request_body["first_name"]
        user.last_name = request_body["last_name"]
        user.email = request_body["email"]
        user.password = request_body["password"]
        return jsonify(user.__dict__)
    else:
        return jsonify({"error": f"User with id {id} not found"}), 404
@user_controller.route("/delete/<id>",methods=["DELETE"])
def delete_user():
    return []