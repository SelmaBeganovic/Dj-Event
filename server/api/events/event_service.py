from typing import Union
from api.events.event_model import Event


class EventService:
    @staticmethod
    def get_events_for_user(user_id: int) -> Union[list[Event], list]:
        return Event.query.filter(Event.user_id == user_id).all()
