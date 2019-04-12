from horoscope_2.horoscope import generate_prophecies
from bottle import route, run, view
from datetime import datetime as dt


@route("/")
@view("predictions")
def index():
    now = dt.now()
    return {
        "date": f"{now.year}-{now.month}-{now.day}",
        "predictions": generate_prophecies(6, 2)
            }


run(
    host="localhost",
    port=8080,
    autoreload=True
)
