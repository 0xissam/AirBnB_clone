#!/usr/bin/python3
from models.base_model import BaseModel


class Review (BaseModel):
    place_id = ""
    text = ""
    user_id = ""
    

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)
