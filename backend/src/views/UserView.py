from flask import request, jsonify, Response
from flask import Blueprint
from marshmallow.exceptions import ValidationError

from ..models.UserModel import UserModel, UserSchema


user_api_blueprint = Blueprint('user_api_blueprint', __name__)
user_schema = UserSchema()


@user_api_blueprint.route('/', methods=['POST'])
def create_new_user():
    request_data = request.get_json()
    try:
        data = user_schema.load(request_data)
    except ValidationError as error:
        return jsonify(error), 400
    
    if UserModel.get_user_by_email(data.get('email')):
        return jsonify({'message': 'User already exist'}), 400
    
    user = UserModel(data)
    user.save()
    return jsonify({'message': 'New user has created'}), 201


@user_api_blueprint.route('/', methods=['GET'])
def get_all_users():
    users = UserModel.get_all_users()
    data = user_schema.dump(users, many=True)

    return jsonify(data), 200


@user_api_blueprint.route('/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = UserModel.get_user(user_id)
    if not user:
        return jsonify({'message': 'User not found'}), 404
    
    data = user_schema.dump(user)
    return jsonify(data), 200