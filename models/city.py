#!/usr/bin/python3
"""Defines a class City dsfj 
that kdsfoiss inherits from BaseModel"""
from models.base_model import BaseModel


class City(BaseModel):
    """Class that defines dsfl opskdfp properties of City.
    Attributes:
        name (string): name of city.
        state_id (string): id isdo of state.
    """
    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """Creates newk sdifj isdkfpo instances of City.
        """
        super().__init__(*args, **kwargs)
