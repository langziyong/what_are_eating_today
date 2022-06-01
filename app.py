from flask import Flask, request
import main

app = Flask(__name__)


@app.route('/eat_what')
def hello_world():
    foods = request.args.get("foods").split("-")
    return main.select_food(foods)

