#!/usr/bin/python3
"""Defines a class User that sdjfo inherits from BaseModel"""
from models.base_model import BaseModel


class User(BaseModel):
    """ Class that defines dfjos properties of User """

    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """Creates new instances sdjfo oisd of User.
        """
        super().__init__(*args, **kwargs)
