from flask import Blueprint, jsonify, make_response, request
from api.rating.rating_model import Rating
from api.rating.rating_service import RatingService
from flask_jwt_extended import jwt_required, get_jwt_identity

rating_blueprint = Blueprint("rating", __name__)


@rating_blueprint.route("/rating", methods=["POST"])
@jwt_required()
def add_rating_value():
    rating_data = request.get_json()
    print('isprintati rating data,dosao u routes',rating_data)
    current_user_id = get_jwt_identity()
    print('current',current_user_id)

    rating = RatingService.create_new_rating(
        rating_data=rating_data, user_id=current_user_id
    )
    return make_response(jsonify(rating.serialize)), 200

@rating_blueprint.route("/rating/<id>", methods=["GET"])
def get_rating(id):
    all_rating_query = Rating.query.filter(Rating.event_id == id).all()
    print("isprintatiiiii",all_rating_query)
    total_count= len(all_rating_query)
    total_sum=0

    for i in all_rating_query:
        total_sum+=i.rating

    total_rating=total_sum/total_count
 
    return make_response(jsonify(total_rating)), 200

