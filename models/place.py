#!/usr/bin/python3
"""Defines a class Place that sdisdkpa inherits from BaseModel"""
from models.base_model import BaseModel


class Place(BaseModel):
    """Class that defineshs sduj properties of Place.

    Attributes:
        city_id (string): id of city sdfij oisdf.
        user_id (string): id of userjsjfis dsjf.
        name (string): name of Place apoaopwei .
        description (string): description of placejsdf.
        number_rooms (integer): number of rooms in place jdsf.
        number_bathrooms (integer): number of sduif bathrooms in place.
        max_guest (integer): maximum number of guests  djsodf allowed in a place.
        price_by_night (integer): price of room perjndf night.
        latitude (float): latitude of place on a koidsfoi sdmap.
        longitude (float): longitude of place on a sudfi map.
        amenity_ids (list (of string)): list of Amenity.idiu wefui of place.
    """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []

    def __init__(self, *args, **kwargs):
        """Creates new instancesj sdufjoi of Place.
        """
        super().__init__(*args, **kwargs)
