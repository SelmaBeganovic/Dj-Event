from crypt import methods
from flask import Blueprint, jsonify, make_response
from api.events.event_model import Event

events_blueprint = Blueprint("events", __name__)


@events_blueprint.route("/events", methods=["GET"])
def events():
    all_events = Event.query.all()
    return jsonify([evt.serialize for evt in all_events])
