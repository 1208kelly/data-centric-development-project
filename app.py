import os
from flask import flask

app = Flask(__name__)


@app.route('/')
def recipe():
    return 'Ven a comer'

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
        port=int(os.environ.get('PORT')),
        debug=True)
