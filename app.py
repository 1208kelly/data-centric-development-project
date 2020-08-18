import os
from flask import Flask, redirect, url_for, render_template, request
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from os import path
if path.exists("env.py"):
    import env


app = Flask(__name__)


app.config["MONGO_DBNAME"] = 'ven_a_comer'
app.config["MONGO_URI"] = 'mongodb+srv://u5erN4me:pa55W0rd@myfirstcluster1208.14c5g.mongodb.net/ven_a_comer?retryWrites=true&w=majority'


mongo = PyMongo(app)


@app.route('/')
@app.route('/get_recipes')
def get_recipes():
    return render_template("recipes.html", recipes=mongo.db.recipes.find())


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
