from typing import Union
from fastapi import FastAPI

from controllers import get_endpoints, get_letter

import json

app = FastAPI()

@app.get("/")
def read_root():
    return get_endpoints()

@app.get("/letter")
def read_generated_letter(to_name = None, from_name = None, subject = None, emotion = None, location = None, timescale = None, when = None, additional = None):
    return get_letter(to_name, from_name, subject, emotion, location, timescale, when, additional)