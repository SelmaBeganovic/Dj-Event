from datetime import datetime
from typing import Dict, List, Optional, Union
from api import db
from api.rating.rating_model import Rating


class RatingService:

    @staticmethod
    def create_new_rating(rating_data: Dict[str,str], user_id):
      
        rating=Rating(
            rating=rating_data.get("rating"), 
            created_at=datetime.now(),
            event_id=rating_data.get("eventId"),
            user_id=user_id,

        )
        db.session.add(rating)
        db.session.commit()
        return rating
