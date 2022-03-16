from flask import Blueprint, jsonify, make_response, request
from api.comment.comment_model import Comment
from api.comment.comment_service import CommentService


comment_blueprint = Blueprint("comment", __name__)


@comment_blueprint.route("/comment", methods=["POST"])
def add_new_comment():
    print("comment*****")
    comment_data = request.get_json()
    print(comment_data)

    comment = CommentService.create_new_comment(
        comment_data=comment_data,
    )
    return make_response(jsonify(comment.serialize)), 200


@comment_blueprint.route("/comment/<id>", methods=["GET"])
def get_comment(id):
    all_comment_query = Comment.query.filter(Comment.event_id == id)
    args = request.args

    all_comment_query = all_comment_query.order_by(Comment.__dict__['created_at'].desc())

    per_page = int(args.get("_limit", 5))
    start = int(args.get("_start", 1))
    comment = all_comment_query.paginate(
        page=start, per_page=per_page, error_out=True
    ).items
    return make_response(jsonify([com.serialize for com in comment])), 200
