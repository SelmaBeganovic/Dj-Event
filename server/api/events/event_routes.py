from flask import Blueprint, jsonify, make_response, request
from api.events.event_model import Event
from api.events.event_service import EventService, DeleteEventException

from flask_jwt_extended import jwt_required, get_jwt_identity

events_blueprint = Blueprint("events", __name__)


@events_blueprint.route("/events", methods=["GET"])
def events():
    all_events_query = Event.query
    args = request.args

    if slug := args.get("slug", None):
        all_events_query = all_events_query.filter(Event.slug == slug)

    if sort_by := args.get("_sort", None):
        fild, direction = sort_by.split(":")

        if direction == "ASC":
            all_events_query = all_events_query.order_by(Event.__dict__[fild].asc())
        elif direction == "DESC":
            all_events_query = all_events_query.order_by(Event.__dict__[fild].desc())

    per_page = int(args.get("_limit", 5))

    start = int(args.get("_start", 1))
    all_events = all_events_query.paginate(
        page=start, per_page=per_page, error_out=True
    ).items

    return make_response(jsonify([evt.serialize for evt in all_events])), 200


@events_blueprint.route("/events", methods=["POST"])
@jwt_required()
def add_new_event():
    current_user_id = get_jwt_identity()
    event_data = request.get_json()

    event = EventService.create_new_event(
        event_data=event_data, user_id=current_user_id
    )

    return make_response(jsonify(event.serialize)), 200


@events_blueprint.route("/events/<id>", methods=["DELETE"])
@jwt_required()
def delete_event(id):
    try:
        EventService.delete_event(id)
        return make_response(jsonify({"message": "Event successfully deleted"})), 200
    except DeleteEventException as e:
        return make_response(jsonify({"message": "Not found"})), 404


@events_blueprint.route("/events/<id>", methods=["GET"])
@jwt_required()
def get_event(id):
    current_user_id = get_jwt_identity()
    event = EventService.get_event_by_id_and_user_id(id, current_user_id)

    if event is None:
        return make_response(jsonify({"message": "Event not found"})), 404

    return make_response(jsonify(event.serialize))


@events_blueprint.route("/events/<id>", methods=["PUT"])
@jwt_required()
def update_event(id):
    current_user_id = get_jwt_identity()
    event_data = request.get_json()
    event = EventService.update_event(
        event_id=id, event_data=event_data, user_id=current_user_id
    )

    if event is None:
        return make_response(jsonify({"message": "Not Authorized"})), 401

    return make_response(jsonify(event.serialize))


@events_blueprint.route("/events/count", methods=["GET"])
def count():
    return make_response(jsonify({"total": EventService.get_event_count()})), 200


@events_blueprint.route("/events/me", methods=["GET"])
@jwt_required()
def user_events():
    current_user_id = get_jwt_identity()
    user_events = EventService.get_events_for_user(current_user_id)
    return jsonify([evt.serialize for evt in user_events])
