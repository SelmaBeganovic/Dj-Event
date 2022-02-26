from flask import Blueprint, jsonify, request
from api.events.event_model import Event
from api.user.user_model import User
from api.events.event_service import EventService

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

    return jsonify([evt.serialize for evt in all_events])


@events_blueprint.route("/events/count", methods=["GET"])
def count():
    return jsonify({"total": Event.query.count()})


@events_blueprint.route("/events/me", methods=["GET"])
@jwt_required()
def user_events():
    current_user_id = get_jwt_identity()
    user = User.query.get(current_user_id)
    events = Event.query.all()
    return jsonify([evt.serialize for evt in events])
