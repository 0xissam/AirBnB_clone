#!/usr/bin/python3
from models.base_model import BaseModel


class User(BaseModel):

    email = ""
    password = ""
    last_name = ""
    first_name = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
