import os
import uuid
from flask import Blueprint, request, make_response, jsonify, current_app

from flask_jwt_extended import jwt_required, get_jwt_identity

from api import db
from api.events.event_service import EventService


media_blueprint = Blueprint("media", __name__)


@media_blueprint.route("/upload", methods=["POST"])
@jwt_required()
def upload_event_image():
    file_data = request.files["files"]
    file_uuid = uuid.uuid4()
    file_name = "-".join([str(file_uuid), file_data.filename])
    target_folder = current_app.config.get("UPLOAD_FOLDER")

    if not os.path.isdir(target_folder):
        os.makedirs(target_folder)

    file_data.save(os.path.join(target_folder, file_name))

    current_user_id = get_jwt_identity()
    event_id = request.form["refId"]
    event = EventService.get_event_by_id_and_user_id(
        event_id=event_id, user_id=current_user_id
    )

    event.image = file_name

    db.session.commit()

    return (
        make_response(
            jsonify(
                {
                    "status": "success",
                    "message": "Successfully logged in.",
                    "statusCode": 200,
                }
            )
        ),
        200,
    )
