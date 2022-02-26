from datetime import datetime
from typing import Dict, Union

from api import db
from api.events.event_model import Event
from api.events.event_util import create_slug


class DeleteEventException(Exception):
    pass


class EventService:
    @staticmethod
    def get_event_count():
        return Event.query.count()

    @staticmethod
    def get_events_for_user(user_id: int) -> Union[list[Event], list]:
        return Event.query.filter(Event.user_id == user_id).all()

    @staticmethod
    def create_new_event(event_data: Dict[str, str], user_id):
        event = Event(
            name=event_data.get("name"),
            venue=event_data.get("venue"),
            slug=create_slug(event_data.get("name")),
            address=event_data.get("address"),
            performers=event_data.get("performers"),
            date=datetime.strptime(event_data.get("date"), "%Y-%m-%d"),
            time=event_data.get("time"),
            description=event_data.get("description"),
            user_id=user_id,
        )
        db.session.add(event)
        db.session.commit()
        return event

    @staticmethod
    def delete_event(id):
        try:
            Event.query.filter(Event.id == id).delete()
            db.session.commit()
        except Exception as e:
            raise DeleteEventException(e)
