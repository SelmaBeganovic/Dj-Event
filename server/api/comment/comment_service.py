from datetime import datetime
from typing import Dict, List, Optional, Union
from api import db
from api.comment.comment_model import Comment


class CommentService:

    @staticmethod
    def create_new_comment(comment_data: Dict[str,str]):
      
        comment=Comment(
            username=comment_data.get("username"),
            comment=comment_data.get("comment"), 
            created_at=datetime.now(),
            event_id=comment_data.get("eventId"),

        )
        db.session.add(comment)
        db.session.commit()
        return comment