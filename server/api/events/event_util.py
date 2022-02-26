from flask import current_app
from slugify import slugify


def create_slug(item: str) -> str:
    return slugify(item, to_lower=True)


def create_image_url(img_name):
    if img_name is None:
        return None

    return f"{current_app.config.get('PREFERRED_URL_SCHEME', 'http')}://{current_app.config.get('SERVER_NAME', 'http://localhost:5000')}/static/uploads/{img_name}"
