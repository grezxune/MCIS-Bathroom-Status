from flask import Flask, render_template
from flask.ext.pymongo import PyMongo

app = Flask(__name__)
mongo = PyMongo(app)

def seed_initial_data():
    with app.app_context():
        mongo.db.bathrooms.save(
                {
                    "name": "Hive Guys",
                    "stalls": 
                        [{"name": "Stall 1", "status": "Available"}, 
                        {"name": "Urinal", "status": "Occupied"}]
                })

def query_initial_data():
    with app.app_context():
        cursor = mongo.db.bathrooms.find()

        for document in cursor:
            print("Printing documents in cursor]n")
            print(document)

#seed_initial_data()
query_initial_data()
