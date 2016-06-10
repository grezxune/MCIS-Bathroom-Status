from flask import Flask, render_template
from flask.ext.pymongo import PyMongo
from pymongo import MongoClient

app = Flask(__name__)
app.config['MONGO_DBNAME'] = 'mcis_bathroom'
mongo = PyMongo(app)
try:
    client = MongoClient()
except errors.ConnectionFailure, e:
    print("Could not connect to MongoDB: %s" % e)

db = client.seed_data

class Bathroom:
    def __init__(self, name):
        self.name = name
        self.stalls = []


class Stall:
    def __init__(self, name):
        self.name = name
        self.status = "TEST"

    def set_status(status):
        self.status = status


@app.route("/")
def index():
    bathroomCursor = db.bathrooms.find()
    bathrooms = []

    for bathroom in bathroomCursor:
        print(bathroom)
        newBathroom = Bathroom(bathroom["name"])
        for stall in bathroom["stalls"]:
            newStall = Stall(stall["name"])
            newStall.status = stall["status"]
            newBathroom.stalls.append(newStall)
        bathrooms.append(newBathroom)

    return render_template("index.html", bathrooms=bathrooms)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port='8000')
