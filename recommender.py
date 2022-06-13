from flask import Flask, request, render_template, redirect, flash, jsonify, url_for
import pandas as pd
import numpy as np
from surprise import dump
from db import DataBase
from recommender import Recommender

app = Flask(__name__)
model = keras.models.load_model("nn.h5")
users = np.load('data/users.npy').item()

recommender = Recommender(db)
attractions = db.get_attractions()
topics = [
        {'id': '0', 'name': 'Landmarks', 'photo': '/static/landmarks.jpg'},
        {'id': '1', 'name': 'Art', 'photo': '/static/art.jpeg'},
        {'id': '2', 'name': 'Tours', 'photo': '/static/tours.jpg'},
        {'id': '3', 'name': 'Food', 'photo': '/static/food.jpg'},
        {'id': '4', 'name': 'Nature', 'photo': '/static/nature.jpg'},
        {'id': '5', 'name': 'Performing\narts', 'photo': '/static/performing.jpg'}
    ]

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST"
    file = request.files.get('file')
    if file is None or file.filename = "":
        return jsonify({"error:"no file})

        try:
            pass
        except Exception as 0:
            return jsonify({"error": str(e)})

    return "OK"
