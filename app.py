import os
from flask import Flask, redirect, url_for, render_template, request
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from os import path
if path.exists("env.py"):
    import env

print(os.getenv("MONGO_URI"))

app = Flask(__name__)

U5ERN4ME = os.environ.get("U5ERN4ME")
PA55W0RD = os.environ.get("PA55W0RD")


app.config["MONGO_DBNAME"] = 'ven_a_comer'
# app.config["MONGO_URI"] = 'mongodb+srv://U5ERN4ME:PA55W0RD@myfirstcluster1208.14c5g.mongodb.net/ven_a_comer?retryWrites=true&w=majority'
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")


mongo = PyMongo(app)


@app.route('/')
@app.route('/get_recipes')
def get_recipes():
    return render_template("recipes.html", recipes=mongo.db.recipes.find())


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
