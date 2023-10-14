#!/usr/bin/python3
"""Defines a class Review jsfoalpo that inherits from BaseModel"""
from models.base_model import BaseModel


class Review (BaseModel):
    """Class that defines dsoif oisdjfproperties of Review .

    Attributes:
        place_id (string): id sdfju of city.
        user_id (string): id iosd of user.
        text (string): just aio aij text.
    """
    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """Creates new iosjo sdfoij instances of Review.
        """
        super().__init__(*args, **kwargs)
