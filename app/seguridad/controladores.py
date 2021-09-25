from flask import request, jsonify
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity

from app.seguridad import seguridad_bp
from app.seguridad.decoradores import admin_requerido


@seguridad_bp.route('/generar-token', methods=["POST"])
def login():
    username = request.json.get("username", None)
    password = request.json.get("password", None)
    if username != "test" or password != "test":
        return jsonify({"msg": "Bad username or password"}), 401

    additional_claims = {'authorities': ['ROLE_USER']}
    access_token = create_access_token(identity=username, additional_claims=additional_claims)
    return jsonify(access_token=access_token)


@seguridad_bp.route("/protected", methods=["GET"])
@jwt_required()
@admin_requerido
def protected():
    # Access the identity of the current user with get_jwt_identity
    current_user = get_jwt_identity()
    return jsonify(logged_in_as=current_user), 200
