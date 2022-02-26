from turtle import st
from slugify import slugify


def create_slug(item: str) -> str:
    return slugify(item, to_lower=True)
